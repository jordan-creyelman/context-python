# Conventions Python

## Simplicité et structure

Python 3.11+, indentation de quatre espaces, noms anglais en snake_case ; classes en PascalCase si utiles. Une fonction a une responsabilité claire. Préférer la bibliothèque standard et une solution courte. KISS, YAGNI, DRY comme dans context-bash.

Un script a une fonction main() et une garde d'entrée. En tools, main() retourne un code entier et la garde appelle `raise SystemExit(main())`. Importer le module ne doit pas exécuter l'outil. Séparer traitement métier et CLI pour tester sans terminal.

## Types et documentation

Annoter les paramètres et retours des fonctions importantes en tools :

```python
from pathlib import Path


def count_errors(path: Path) -> int:
    ...
```

Préférer le typage moderne Python 3.11+ : `list[str]`, `dict[str, int]`, `tuple[str, ...]`, `str | None`. Éviter `Any` sauf lorsqu'il est réellement nécessaire. Annoter les variables locales seulement lorsque le type n'est pas évident ou améliore la compréhension.

Une annotation n'empêche pas une valeur invalide à l'exécution. Valider explicitement les données externes. Les types documentent les interfaces ; ils ne remplacent ni validation, ni gestion d'erreurs, ni tests.

Une docstring décrit le contrat, les limites ou exceptions utiles ; éviter de paraphraser chaque ligne. Introduire ces notions progressivement en learning.

## Entrées et validation

Considérer comme non fiables les entrées utilisateur, fichiers, variables d'environnement, réseau et API. Valider les données aux frontières du programme avant de les transmettre à la logique métier.

Utiliser argparse pour l'aide et les arguments, pathlib pour les chemins. Vérifier valeurs, plages et format avant action. Un contrôle préalable d'existence ne garantit pas la lecture : le fichier peut changer entre contrôle et ouverture.

## Gestion d'erreurs

Traiter les erreurs attendues avec l'exception la plus précise possible : `ValueError` pour une valeur invalide, `FileNotFoundError` pour un fichier absent, `OSError` pour les erreurs d'E/S, `UnicodeError` pour les problèmes d'encodage, ou une exception métier claire lorsque le domaine le justifie.

Ne pas masquer une erreur avec `except Exception: pass`, un bloc vide ou une valeur par défaut trompeuse. Ne capturer `Exception` que lorsqu'une frontière du programme doit convertir une erreur inconnue en diagnostic contrôlé ; dans ce cas, conserver l'information utile via logging et retourner un échec explicite.

Utiliser `with path.open(encoding="utf-8") as stream:` ; parcourir les lignes évite de charger un journal entier en mémoire. Ne pas ignorer les erreurs d'encodage silencieusement.

## Sorties, logging et effets

stdout contient le résultat ; stderr contient les diagnostics. Configurer logging dans main(), utiliser un logger de module. INFO pour une information utile, DEBUG pour des détails activables, ERROR pour un échec. Pas de configuration globale à l'import, pas de secrets dans les messages.

Documenter les codes : 0 succès, 1 échec opérationnel, 2 mauvaise utilisation lorsque cette convention convient. Un résultat vide ou zéro peut être un succès.

Pour les écritures, refuser l'écrasement par défaut et expliquer l'effet ; proposer --dry-run pour les actions qui en bénéficient. Tester sur données fictives. Si une commande externe est nécessaire, utiliser subprocess avec une liste d'arguments, vérifier son statut et signaler la dépendance ; éviter shell=True. Préciser les dépendances de plateforme et les limites de portabilité.

## Stratégie de tests

Ajouter uniquement les tests utiles au comportement du programme.

Ordre de priorité :
1. test du cas nominal ;
2. test des cas limites pertinents ;
3. test des entrées invalides ;
4. test des erreurs opérationnelles importantes ;
5. test de non-régression après correction d'un bug.

Privilégier les tests unitaires rapides pour la logique métier isolée. Ajouter un test d'intégration seulement lorsqu'il apporte une vraie valeur en vérifiant l'interaction entre plusieurs composants, par exemple logique + système de fichiers, client + service ou CLI + fonction métier.

Pour une CLI, vérifier aussi les arguments, stdout/stderr et le code de sortie lorsque cela fait partie du contrat.

Utiliser `unittest` par défaut pour rester dans la bibliothèque standard. Utiliser pytest uniquement si le projet l'utilise déjà ou si son apport est justifié. Utiliser des fichiers et dossiers temporaires pour isoler les tests. Aucun test destructif sur des données réelles.

## Vérification du script de référence

```bash
python3 -m compileall -q projects tests
python3 -m unittest discover -s tests -v
python3 projects/log_summary.py --help
```

La compilation vérifie la syntaxe, pas le comportement ni les types. Les tests vérifient la logique et la CLI avec fichiers temporaires : plusieurs erreurs, zéro correspondance, fichier vide, fichier absent, dossier à la place du fichier, UTF-8 invalide, chemin avec espaces et argument absent.

Si le projet possède déjà un outil de typage, l'exécuter également. mypy/pyright et Ruff restent facultatifs si disponibles ; aucune installation imposée. Annoncer uniquement les résultats réellement observés.
