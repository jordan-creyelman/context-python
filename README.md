# context-python

Contexte réutilisable pour apprendre Python et produire de petits outils utiles, notamment pour Linux et l'administration système. Inspiré de [context-bash](https://github.com/jordan-creyelman/context-bash) : même approche simple, progressive et pragmatique.

Explications en français ; code, commentaires, docstrings et messages des scripts en anglais.

## Modes

| Mode | Objectif | Fichier principal |
| --- | --- | --- |
| `learning` | Apprendre progressivement, un exercice à la fois | [docs/learning.md](docs/learning.md) |
| `tools` | Produire un script directement utilisable | [docs/tools.md](docs/tools.md) |

Le choix du mode et les règles communes sont centralisés dans [AGENTS.md](AGENTS.md).

## Structure

```text
context-python/
├── AGENTS.md
├── README.md
├── docs/
│   ├── learning.md
│   ├── tools.md
│   ├── roadmap.md
│   ├── progress.md
│   ├── conventions.md
│   └── architecture.md
├── cheatsheets/
│   ├── python.md
│   └── files-cli.md
├── exercises/
│   └── README.md
├── projects/
│   ├── README.md
│   └── log_summary.py
└── tests/
    └── test_log_summary.py
```

## Repères

- [docs/conventions.md](docs/conventions.md) : conventions Python, validation, erreurs, logging et tests.
- [docs/architecture.md](docs/architecture.md) : architecture progressive, `src/`, Clean Architecture et DDD.
- [docs/roadmap.md](docs/roadmap.md) : progression d'apprentissage.
- [docs/progress.md](docs/progress.md) : acquis réellement validés.
- [cheatsheets/python.md](cheatsheets/python.md) : mémo Python.
- [cheatsheets/files-cli.md](cheatsheets/files-cli.md) : fichiers, argparse et tests.
- [projects/log_summary.py](projects/log_summary.py) : script de référence du mode `tools`.

## Utilisation

Pour apprendre :

> Lis AGENTS.md puis applique le mode learning de context-python. Reprends depuis ma progression validée et donne un seul exercice.

Pour produire un outil :

> Lis AGENTS.md puis applique le mode tools de context-python. Crée un script qui compte les lignes ERROR d'un journal UTF-8 avec les tests essentiels.

## Environnement de référence

Python **3.11+**. Les exemples fournis utilisent uniquement la bibliothèque standard.

Depuis la racine du dépôt :

```bash
python3 projects/log_summary.py --help
python3 -m unittest discover -s tests -v
python3 -m compileall -q projects tests
```

Sur Windows, utiliser `py -3` si nécessaire.
