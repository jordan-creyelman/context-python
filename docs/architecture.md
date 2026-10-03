# Architecture Python pragmatique

Objectif : garder une architecture aussi simple que possible, puis la faire évoluer seulement lorsque le besoin réel apparaît.

## Principe général

Commencer petit. Ajouter un module, une classe, une couche ou une abstraction uniquement si cela réduit réellement la complexité, améliore les tests ou clarifie les responsabilités.

Éviter les architectures imposées par habitude. KISS et YAGNI priment sur les patterns.

## Niveau 1 — Petit script

Pour un besoin simple, un seul fichier suffit :

```text
project/
└── main.py
```

Séparer le code en petites fonctions. Garder `main()` pour l'orchestration et éviter d'y placer toute la logique métier.

Exemple de séparation dans un seul fichier :

```python
def load_data() -> list[str]:
    ...


def process_data(items: list[str]) -> int:
    ...


def main() -> int:
    items = load_data()
    result = process_data(items)
    print(result)
    return 0
```

Ne pas créer plusieurs fichiers tant que cela n'améliore pas réellement la lisibilité ou les tests.

## Niveau 2 — Projet en plusieurs modules

Quand un fichier devient difficile à lire, séparer par responsabilité.

Exemple minimal :

```text
project/
├── main.py
├── domain.py
├── services.py
├── storage.py
└── tests/
```

Responsabilités possibles :

- `domain.py` : règles métier et concepts principaux ;
- `services.py` : orchestration des cas d'utilisation ;
- `storage.py` : fichiers, base de données ou persistance ;
- `main.py` : CLI, configuration et démarrage ;
- `tests/` : tests du comportement.

Ne pas créer un fichier par classe ou par fonction sans raison.

## Séparation des responsabilités

Séparer autant que possible :

- logique métier ;
- interface utilisateur ou CLI ;
- stockage ;
- réseau et API ;
- configuration ;
- infrastructure système.

La logique métier doit rester testable sans terminal, réseau, base de données ou fichiers réels lorsque cela est raisonnable.

## Dépendances

Les dépendances doivent aller vers la logique métier, pas l'inverse.

Une fonction métier ne devrait pas importer directement une CLI, une bibliothèque de base de données ou un client HTTP si cela peut être évité simplement.

Préférer passer les données ou dépendances nécessaires en paramètres.

## Fonctions, classes et composition

Utiliser des fonctions par défaut lorsqu'elles suffisent.

Créer une classe lorsqu'elle représente clairement un concept avec un état et des comportements associés.

Préférer la composition à l'héritage. Utiliser l'héritage seulement lorsqu'il existe une vraie relation "est un" et qu'il simplifie le modèle.

Éviter les classes uniquement destinées à regrouper des fonctions statiques.

## Structure `src/`

Ne pas imposer `src/` à un petit script ou à un projet pédagogique simple.

Utiliser une structure `src/` lorsqu'un projet devient un vrai package installable ou comporte plusieurs modules destinés à être importés :

```text
project/
├── pyproject.toml
├── src/
│   └── my_app/
│       ├── __init__.py
│       ├── domain.py
│       ├── services.py
│       └── cli.py
└── tests/
```

Ajouter `pyproject.toml` seulement lorsqu'un besoin réel de packaging, dépendances ou configuration d'outils apparaît.

## Clean Architecture

Utiliser Clean Architecture seulement lorsque la taille ou la complexité du projet le justifie.

Direction générale :

```text
domain
  ↓
use_cases / services
  ↓
interfaces / adapters
  ↓
infrastructure
```

Le domaine contient les règles métier et ne dépend pas de l'infrastructure.

Les couches externes peuvent dépendre des couches internes, mais l'inverse doit être évité.

Pour un petit outil CLI, une séparation simple entre logique métier, CLI et stockage est généralement suffisante.

## DDD

Utiliser DDD uniquement lorsqu'il existe un domaine métier réellement complexe et un vocabulaire métier important.

Introduire progressivement :

- entités lorsqu'une identité métier est nécessaire ;
- Value Objects pour des concepts immuables avec règles propres ;
- agrégats seulement pour de vraies frontières de cohérence ;
- repositories lorsque la persistance doit être abstraite du domaine ;
- services de domaine lorsqu'une règle métier ne correspond naturellement à aucune entité.

Ne pas transformer un simple CRUD ou script d'administration en architecture DDD.

## Tests et architecture

L'architecture doit faciliter les tests, pas les compliquer.

Privilégier :

- tests unitaires sur la logique métier ;
- tests d'intégration aux frontières réelles utiles ;
- peu de mocks ;
- dépendances simples à remplacer lorsque nécessaire.

Une difficulté excessive à tester est souvent un signal qu'une fonction ou un module possède trop de responsabilités.

## Progression recommandée

Apprendre l'architecture progressivement, lorsque la roadmap y arrive :

1. un fichier avec plusieurs fonctions ;
2. séparation entre logique et `main()` ;
3. extraction d'un premier module ;
4. séparation métier / CLI ;
5. séparation stockage ou réseau ;
6. gestion claire des dépendances ;
7. structure `src/` pour un vrai package ;
8. Clean Architecture sur un projet suffisamment complexe ;
9. DDD seulement sur un domaine qui le justifie.

Ne jamais introduire l'étape suivante uniquement pour rendre le projet plus "professionnel".
