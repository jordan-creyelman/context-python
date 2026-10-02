# context-python

Contexte réutilisable pour apprendre Python et produire de petits outils utiles, notamment pour Linux et l'administration système. Inspiré de [context-bash](https://github.com/jordan-creyelman/context-bash) : même structure, KISS, YAGNI et DRY. Explications en français ; code, commentaires, docstrings et messages des scripts en anglais.

## Deux modes explicites

| Mode | Objectif | Réponse attendue |
| --- | --- | --- |
| `learning` | Apprendre progressivement | Théorie courte, exemple concret, un seul exercice, attente de la tentative, indices et correction pédagogique |
| `tools` | Obtenir un outil utilisable | Script complet, typé, entrées validées, erreurs explicites, logging utile, docstrings et tests essentiels |

Annoncer le mode actif. Une demande explicite de mode prime. Sinon, apprendre/comprendre/s'entraîner active `learning` ; demander un script utilisable active `tools`. Si le besoin est ambigu, demander le mode avant de proposer une activité. Un changement de mode doit être explicite ; le mode `tools` ne valide pas automatiquement un acquis.

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
│   └── conventions.md
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

[AGENTS.md](AGENTS.md) définit les instructions communes et le choix du mode. Les contextes [learning](docs/learning.md) et [tools](docs/tools.md) précisent les réponses attendues. Consulter la [feuille de route](docs/roadmap.md), la [progression](docs/progress.md), les [conventions](docs/conventions.md), les fiches [Python](cheatsheets/python.md) et [fichiers/CLI](cheatsheets/files-cli.md), puis les [exercices](exercises/README.md) ou [projets](projects/README.md) utiles.

## Utiliser ce contexte

Donner accès au dépôt ou joindre les fichiers utiles. Nommer le dépôt ne garantit pas que l'assistant puisse le lire.

> Lis AGENTS.md, README.md, docs/conventions.md, docs/learning.md, docs/roadmap.md et docs/progress.md de context-python. Mode learning : je débute, propose le premier exercice et attends ma tentative.

> Lis AGENTS.md, README.md, docs/conventions.md et docs/tools.md de context-python. Mode tools : crée un script complet qui compte les lignes ERROR d'un journal UTF-8, avec usage et tests essentiels.

Pour reprendre : indiquer le mode, les acquis et le dernier exercice, ou donner accès à docs/progress.md. Ce fichier n'est mis à jour qu'après validation réelle ; aucune mémoire automatique n'est supposée.

## Environnement et vérification

Python **3.11 ou plus récent** ; bibliothèque standard uniquement pour les exemples fournis. Vérifier avec `python3 --version`. Les commandes ci-dessous partent de la racine du dépôt (sur Windows, utiliser `py -3` si nécessaire).

```bash
python3 projects/log_summary.py --help
python3 projects/log_summary.py "/tmp/my folder/app.log" --verbose
python3 -m unittest discover -s tests -v
python3 -m compileall -q projects tests
```

Le journal est un fichier fourni par l'utilisateur ; aucun accès privilégié nécessaire. Le script compte les lignes commençant exactement par `ERROR `, affiche le total sur stdout et les diagnostics sur stderr. Code 0 : succès, 1 : erreur de lecture ou d'encodage, 2 : arguments invalides. Un total nul est un succès.

KISS : rester simple. YAGNI : répondre au besoin présent. DRY : éviter les répétitions réelles. Aucun framework, CI ou dépendance supplémentaire sans besoin concret.
