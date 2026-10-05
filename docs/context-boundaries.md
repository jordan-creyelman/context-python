# Context boundaries

## Principle

Pour une tâche multi-domaine, définir :

1. un **contexte principal** ;
2. zéro ou plusieurs **contextes secondaires** réellement utiles.

Le contexte principal possède l'objectif, la roadmap et la progression principales de la tâche.

## Python ownership

`context-python` est la source de vérité pour :

- syntaxe et concepts Python ;
- qualité du code Python ;
- typing ;
- exceptions ;
- tests Python ;
- debugging Python ;
- architecture Python ;
- progression d'apprentissage Python.

## Secondary contexts

### context-github

Source de vérité pour :

- Git ;
- GitHub ;
- branches ;
- commits ;
- staging ;
- pull requests ;
- reviews ;
- merges ;
- tags ;
- CI liée au workflow GitHub.

### context-security

Source de vérité pour :

- règles de sécurité ;
- validation de frontières ;
- gestion des secrets ;
- menaces et risques ;
- critères de sécurité.

Le code Python utilisé pour appliquer ces règles reste évalué côté `context-python`.

### context-maker

Source de vérité pour :

- besoin matériel ;
- contraintes maker ;
- interactions avec le matériel ;
- objectifs du projet physique.

## Shared project evidence

Un même projet peut produire plusieurs preuves.

Exemple :

```text
Secure Python CLI
├── Python exception handling → context-python
├── input validation security → context-security
└── commit workflow → context-github
```

Chaque contexte ne met à jour que les compétences qu'il possède.

## Conflict rule

Si deux contextes semblent se contredire :

1. identifier le domaine propriétaire ;
2. appliquer sa règle ;
3. utiliser les autres contextes comme contraintes complémentaires ;
4. éviter de copier la même règle dans plusieurs repos.

Python manages Python. Chaque domaine gère sa propre progression.
