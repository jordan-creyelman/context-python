# Conventions Python à apprendre progressivement

Ce fichier décrit la cible de qualité du code. Ne pas imposer toutes ces règles dès les premiers exercices : les introduire selon [roadmap.md](roadmap.md).

## Simplicité et style

Python 3.11+, indentation de quatre espaces, noms anglais en `snake_case` ; classes en `PascalCase` lorsqu'elles sont utiles.

- KISS, YAGNI et DRY.
- Une fonction possède une responsabilité claire.
- Préférer la bibliothèque standard.
- Respecter PEP 8 sans sacrifier la lisibilité.

Pour un script complet, utiliser `main()` et une garde d'entrée. Importer un module ne doit pas déclencher l'exécution du programme.

## Types et documentation

Quand le typage est étudié, annoter les paramètres et retours importants :

```python
from pathlib import Path


def count_errors(path: Path) -> int:
    ...
```

Préférer le typage moderne : `list[str]`, `dict[str, int]`, `tuple[str, ...]`, `str | None`.

Éviter `Any` sauf nécessité réelle. Les annotations documentent un contrat mais ne valident pas les données à l'exécution.

Une docstring explique le contrat, une limite ou une exception utile ; elle ne paraphrase pas chaque ligne.

## Entrées et validation

Considérer comme non fiables les entrées utilisateur, fichiers, variables d'environnement, réseau et API.

Valider les données aux frontières du programme.

Lorsque la CLI est étudiée :

- utiliser `argparse` pour les arguments ;
- utiliser `pathlib` pour les chemins ;
- vérifier valeurs, plages et formats avant action.

## Gestion d'erreurs

Utiliser l'exception la plus précise adaptée au problème : `ValueError`, `FileNotFoundError`, `OSError`, `UnicodeError` ou une exception métier justifiée.

Ne jamais masquer une erreur avec `except Exception: pass`, un bloc vide ou une valeur trompeuse.

Capturer `Exception` seulement à une frontière du programme lorsqu'il faut convertir une erreur inconnue en diagnostic contrôlé tout en conservant l'information utile.

## Fichiers et ressources

Utiliser `with` pour les ressources qui doivent être libérées.

Pour les fichiers texte, préciser l'encodage lorsque c'est pertinent :

```python
with path.open(encoding="utf-8") as stream:
    for line in stream:
        ...
```

Ne pas ignorer silencieusement les erreurs d'encodage.

## Sorties et logging

Lorsque ces notions sont étudiées :

- stdout contient le résultat ;
- stderr contient les diagnostics ;
- configurer le logging dans `main()` ;
- ne jamais journaliser de secret.

Pour une CLI, documenter les codes de sortie lorsque cela apporte une valeur réelle.

## Tests

Ajouter les tests qui apportent une information utile :

1. cas nominal ;
2. cas limite pertinent ;
3. entrée invalide ;
4. erreur opérationnelle importante ;
5. test de non-régression après correction d'un bug.

Privilégier les tests unitaires rapides. Ajouter un test d'intégration seulement lorsqu'il vérifie une interaction réelle utile.

Utiliser `unittest` par défaut pour rester dans la bibliothèque standard. Utiliser pytest lorsqu'un projet l'utilise déjà ou lorsque son apport a été étudié et justifié.

Tester avec des fichiers et dossiers temporaires. Aucun test destructif sur des données réelles.

## Vérification

Pour les projets fournis dans ce dépôt :

```bash
python3 -m compileall -q projects tests
python3 -m unittest discover -s tests -v
```

La compilation vérifie la syntaxe, pas le comportement ni les types.

Les outils de typage ou de lint comme mypy, pyright ou Ruff sont introduits seulement lorsqu'ils apportent une valeur pédagogique ou qu'un projet les utilise déjà.
