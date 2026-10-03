# context-python

Contexte réutilisable consacré à **l'apprentissage de Python** : théorie courte, pratique progressive, un exercice à la fois et validation réelle des acquis.

Explications en français ; code, commentaires, docstrings et messages des scripts en anglais.

## Principe

Le dépôt n'a qu'un objectif : apprendre Python correctement, des bases jusqu'aux notions avancées utiles.

La qualité du code fait partie de l'apprentissage : typage, gestion d'erreurs, tests, architecture et design patterns sont introduits progressivement lorsqu'ils deviennent pertinents.

## Structure

```text
context-python/
├── AGENTS.md
├── README.md
├── docs/
│   ├── learning.md
│   ├── roadmap.md
│   ├── progress.md
│   ├── conventions.md
│   ├── architecture.md
│   ├── theory.md
│   ├── workflow.md
│   ├── testing.md
│   ├── debugging.md
│   └── anti-patterns.md
├── cheatsheets/
│   ├── python.md
│   └── files-cli.md
├── DECISIONS.md
├── checklists/
│   └── project-completion.md
├── exercises/
│   └── README.md
├── projects/
│   ├── README.md
│   ├── maker-inventory.md
│   └── log_summary.py
└── tests/
    └── test_log_summary.py
```

## Repères

- [AGENTS.md](AGENTS.md) : règles générales du contexte.
- [docs/learning.md](docs/learning.md) : méthode pédagogique.
- [docs/roadmap.md](docs/roadmap.md) : ordre des notions.
- [docs/progress.md](docs/progress.md) : acquis réellement validés.
- [docs/conventions.md](docs/conventions.md) : bonnes pratiques Python à apprendre progressivement.
- [docs/architecture.md](docs/architecture.md) : architecture pragmatique pour les étapes avancées.
- [cheatsheets/python.md](cheatsheets/python.md) : mémo Python.
- [cheatsheets/files-cli.md](cheatsheets/files-cli.md) : fichiers, CLI et tests.
- [projects/log_summary.py](projects/log_summary.py) : projet de référence à étudier lorsque les prérequis sont acquis.

## Utilisation

Exemple :

> Lis AGENTS.md et le contexte de context-python. Reprends depuis ma progression validée, donne-moi la théorie essentielle puis un seul exercice.

Pour travailler une notion précise :

> Utilise context-python pour m'apprendre les exceptions. Théorie courte puis un exercice à la fois.

## Environnement

Python **3.11+** pour les exemples actuels. La bibliothèque standard est privilégiée.

Pour vérifier les projets fournis :

```bash
python3 -m compileall -q projects tests
python3 -m unittest discover -s tests -v
```

Sur Windows, utiliser `py -3` si nécessaire.

## Compléments pratiques

- [Théorie](docs/theory.md) et [parcours inventaire maker](projects/maker-inventory.md) : besoin → notion → roadmap → preuve.
- [Workflow professionnel](docs/workflow.md) : petites modifications, Git, commits et revue.
- [Tests](docs/testing.md) : choisir les comportements utiles à vérifier.
- [Débogage](docs/debugging.md) : symptôme → hypothèse → test → correction → vérification.
- [Erreurs classiques](docs/anti-patterns.md) : conséquences et habitudes utiles.
- [Checklist de fin de projet](checklists/project-completion.md) : clôture adaptée aux notions étudiées.
- [DECISIONS.md](DECISIONS.md) : expliquer les choix et leurs conséquences.

La progression distingue **TODO / Learning / Practiced / Validated** sans cocher de nouvel acquis automatiquement. Les règles pédagogiques restent dans AGENTS.md et docs/learning.md ; les fiches servent de références ciblées.
