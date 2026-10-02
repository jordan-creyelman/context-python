# Conventions Python

## Simplicité et structure

Python 3.11+, indentation de quatre espaces, noms anglais en snake_case ; classes en PascalCase si utiles. Une fonction a une responsabilité claire. Préférer la bibliothèque standard et une solution courte. KISS, YAGNI, DRY comme dans context-bash.

Un script a une fonction main() et une garde d'entrée. En tools, main() retourne un code entier et la garde appelle `raise SystemExit(main())`. Importer le module ne doit pas exécuter l'outil. Séparer traitement métier et CLI pour tester sans terminal.

## Types et documentation

Annoter paramètres et retours des fonctions en tools : `def count_errors(path: Path) -> int:`. Une annotation n'empêche pas une valeur invalide à l'exécution. Valider explicitement les données externes. Une docstring décrit le contrat, les limites ou exceptions utiles ; éviter de paraphraser chaque ligne. Introduire ces notions progressivement en learning.

## Entrées et erreurs

Utiliser argparse pour l'aide et les arguments, pathlib pour les chemins. Vérifier valeurs, plages et format avant action. Un contrôle préalable d'existence ne garantit pas la lecture : le fichier peut changer entre contrôle et ouverture. Traiter OSError lors de l'opération et UnicodeError pour un fichier texte à encodage imposé. Ne pas masquer une erreur avec `pass` ou une valeur zéro trompeuse.

Utiliser `with path.open(encoding="utf-8") as stream:` ; parcourir les lignes évite de charger un journal entier en mémoire. Ne pas ignorer les erreurs d'encodage silencieusement.

## Sorties, logging et effets

stdout contient le résultat ; stderr contient les diagnostics. Configurer logging dans main(), utiliser un logger de module. INFO pour une information utile, DEBUG pour des détails activables, ERROR pour un échec. Pas de configuration globale à l'import, pas de secrets dans les messages.

Documenter les codes : 0 succès, 1 échec opérationnel, 2 mauvaise utilisation lorsque cette convention convient. Un résultat vide ou zéro peut être un succès.

Pour les écritures, refuser l'écrasement par défaut et expliquer l'effet ; proposer --dry-run pour les actions qui en bénéficient. Tester sur données fictives. Si une commande externe est nécessaire, utiliser subprocess avec une liste d'arguments, vérifier son statut et signaler la dépendance ; éviter shell=True. Préciser les dépendances de plateforme et les limites de portabilité.

## Vérification du script de référence

```bash
python3 -m compileall -q projects tests
python3 -m unittest discover -s tests -v
python3 projects/log_summary.py --help
```

La compilation vérifie la syntaxe, pas le comportement ni les types. Les tests vérifient la logique et la CLI avec fichiers temporaires : plusieurs erreurs, zéro correspondance, fichier vide, fichier absent, dossier à la place du fichier, UTF-8 invalide, chemin avec espaces et argument absent. Annoncer les résultats observés. Ruff/mypy restent facultatifs si disponibles ; aucune installation imposée.
