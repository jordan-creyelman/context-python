# Théorie Python — Junior à Medium

Cette fiche sert de référence théorique. Elle complète la roadmap sans remplacer la pratique : apprendre une notion, l'expliquer simplement, puis l'utiliser dans un exercice ou un projet.

## Niveau Junior

### 1. Types et modèle de données

À connaître :

- `int`, `float`, `str`, `bool`, `None`;
- conversions explicites avec `int()`, `float()`, `str()`, `bool()`;
- objets mutables et immuables;
- valeurs truthy et falsy;
- différence entre valeur, type et référence.

Idée clé : Python est dynamiquement typé, mais chaque objet possède un type à l'exécution.

### 2. Collections

Structures principales :

- `list` : collection ordonnée et mutable;
- `tuple` : collection ordonnée et immuable;
- `dict` : association clé → valeur;
- `set` : ensemble de valeurs uniques.

Savoir choisir la structure adaptée avant d'écrire l'algorithme.

### 3. Contrôle de flux

À maîtriser :

- `if / elif / else`;
- `for` et `while`;
- `break` et `continue`;
- `range()`;
- `enumerate()`;
- `zip()`.

Une boucle doit avoir un objectif clair et une condition d'arrêt compréhensible.

### 4. Fonctions et portée

Une fonction doit avoir une responsabilité claire.

À connaître :

- paramètres et arguments;
- `return`;
- arguments nommés;
- valeurs par défaut;
- `*args` et `**kwargs` lorsqu'ils sont utiles;
- portée locale et globale;
- différence entre retourner une valeur et l'afficher.

Préférer plusieurs petites fonctions cohérentes à une fonction qui fait tout.

### 5. Compréhensions

À connaître :

- list comprehensions;
- dict comprehensions;
- set comprehensions.

Une compréhension est utile pour une transformation simple. Préférer une boucle normale si la logique devient difficile à lire.

### 6. Chaînes de caractères

À maîtriser :

- indexation et slicing;
- méthodes courantes de `str`;
- `split()`, `join()`, `strip()`;
- f-strings;
- validation simple de texte.

### 7. Exceptions

À connaître :

- `try`;
- `except`;
- `else`;
- `finally`;
- `raise`;
- exceptions spécifiques.

Ne jamais masquer silencieusement une erreur avec `except: pass`.

Capturer l'erreur la plus précise possible.

### 8. Modules, packages et environnement

À connaître :

- `import`;
- création de modules;
- packages simples;
- `if __name__ == "__main__":`;
- environnements virtuels;
- `pip`;
- séparation entre code importable et point d'entrée.

Importer un module ne doit pas lancer le programme par surprise.

### 9. Fichiers et données

À connaître :

- `with open(...)`;
- encodage UTF-8;
- `pathlib`;
- lecture et écriture;
- JSON;
- CSV.

Les fichiers sont des entrées externes : leur contenu et leur existence doivent être considérés comme non fiables.

### 10. Typage

Exemple :

```python
def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b
```

À connaître :

- annotations de paramètres et retours;
- `list[str]`;
- `dict[str, int]`;
- `tuple[str, ...]`;
- `str | None`.

Les annotations documentent un contrat mais ne valident pas automatiquement les données à l'exécution.

### 11. POO de base

À connaître :

- classe et objet;
- attribut;
- méthode;
- `__init__`;
- encapsulation;
- composition;
- héritage seulement lorsqu'il simplifie réellement le modèle;
- `dataclass`.

Préférer des fonctions tant qu'une classe n'apporte pas une vraie valeur.

### 12. Qualité du code

Principes :

- PEP 8;
- noms explicites;
- petites fonctions;
- responsabilités claires;
- KISS;
- YAGNI;
- DRY;
- docstrings en anglais lorsque pertinentes.

La lisibilité passe avant la sophistication.

### 13. Tests

À connaître :

- rôle d'un test;
- Arrange / Act / Assert;
- cas nominal;
- cas limite;
- erreur attendue;
- test de non-régression.

Le dépôt utilise `unittest` par défaut. Étudier `pytest` lorsqu'un projet l'utilise déjà ou lorsque son apport est compris.

## Niveau Junior+

### 14. Références, égalité et copies

À comprendre :

- affecter une variable peut créer une nouvelle référence vers le même objet;
- `==` compare des valeurs;
- `is` compare l'identité;
- shallow copy;
- deep copy.

Exemple :

```python
a = []
b = a
b.append("ESP32")

print(a)  # ['ESP32']
```

`a` et `b` référencent ici la même liste.

### 15. Itérables et itérateurs

À connaître :

- iterable;
- iterator;
- `iter()`;
- `next()`;
- protocole d'itération.

Une boucle `for` consomme un itérable sans qu'il soit nécessaire de gérer `next()` manuellement.

### 16. Générateurs

À connaître :

- `yield`;
- lazy evaluation;
- consommation progressive;
- intérêt pour la mémoire.

Utiliser un générateur lorsque toutes les valeurs n'ont pas besoin d'être chargées en mémoire en même temps.

### 17. Décorateurs

À comprendre :

- une fonction est un objet;
- une fonction peut être passée à une autre fonction;
- wrapper;
- syntaxe `@decorator`.

Un décorateur ajoute un comportement transversal sans mélanger ce comportement à la logique métier.

### 18. Context managers

À comprendre :

- rôle de `with`;
- acquisition et libération d'une ressource;
- nettoyage garanti même lorsqu'une erreur survient.

### 19. Dunder methods

À connaître progressivement :

- `__str__`;
- `__repr__`;
- `__len__`;
- `__eq__`.

Ces méthodes définissent comment un objet interagit avec certains mécanismes natifs de Python.

### 20. Collections spécialisées

À connaître lorsque le besoin apparaît :

- `Counter`;
- `defaultdict`;
- `deque`.

Ne pas utiliser une collection spécialisée si une structure native simple suffit.

### 21. Enum

Utiliser `Enum` lorsqu'un concept accepte un ensemble fini de valeurs nommées.

```python
from enum import Enum


class StockStatus(Enum):
    AVAILABLE = "available"
    LOW = "low"
    OUT = "out"
```

## Niveau Medium

### 22. Architecture

Séparer progressivement :

- logique métier;
- cas d'utilisation ou services;
- interface / CLI;
- stockage;
- réseau;
- infrastructure.

Les dépendances doivent rester simples et aller autant que possible vers la logique métier.

Utiliser Clean Architecture seulement si la complexité du projet la justifie.

### 23. Composition, abstraction et polymorphisme

À approfondir :

- composition plutôt qu'héritage par défaut;
- polymorphisme;
- duck typing;
- `Protocol`;
- `ABC` lorsqu'une abstraction explicite apporte une vraie valeur.

SOLID est un guide, pas une obligation. L'appliquer seulement lorsqu'il simplifie réellement le design.

### 24. Typing avancé

À connaître progressivement :

- `Protocol`;
- `TypeVar`;
- `Generic`;
- `Literal`;
- `TypedDict`;
- `Callable`.

Éviter les types avancés si une annotation simple exprime déjà correctement le contrat.

### 25. Exceptions métier

Créer une exception personnalisée lorsqu'elle représente réellement une erreur du domaine et améliore la compréhension du code.

Éviter les hiérarchies d'exceptions complexes sans besoin réel.

### 26. Tests intermédiaires

À connaître :

- fixtures;
- mocks;
- monkeypatch;
- tests d'intégration;
- tests de non-régression;
- isolation des dépendances externes.

Privilégier les tests unitaires rapides et utiliser peu de mocks.

### 27. Logging

Niveaux principaux :

- DEBUG;
- INFO;
- WARNING;
- ERROR;
- CRITICAL.

Le logging sert aux diagnostics techniques. `print()` sert plutôt à une sortie utilisateur simple ou au résultat d'une CLI.

Ne jamais journaliser de secret.

### 28. Concurrence

Comprendre les différences entre :

- threads;
- processus;
- `asyncio`;
- `async / await`.

Choisir selon le problème : I/O, CPU, simplicité et contraintes du projet.

Ne pas rendre du code asynchrone sans besoin concret.

### 29. Performance et Big-O

Connaître les ordres de grandeur courants :

- O(1);
- O(n);
- O(n log n);
- O(n²).

Mesurer avant d'optimiser.

À connaître :

- coût des recherches et parcours;
- consommation mémoire;
- générateurs;
- profiling.

### 30. Environnements Python et uv

À connaître progressivement :

- environnement virtuel ;
- différence entre Python système et environnement de projet ;
- dépendances directes et transitives ;
- `pyproject.toml` ;
- lockfile ;
- création et synchronisation d'un environnement avec `uv` ;
- ajout et suppression de dépendances ;
- exécution d'une commande ou d'un script dans l'environnement du projet ;
- reproductibilité d'un environnement sur une autre machine.

Idée clé : `uv` simplifie la gestion d'un projet Python moderne, mais il ne remplace pas la compréhension des notions d'environnement virtuel, dépendance et packaging.

Apprendre les commandes `uv` dans un projet concret lorsque des dépendances externes deviennent réellement nécessaires. Ne pas ajouter une dépendance uniquement pour pratiquer l'outil.

### 31. Packaging

À connaître :

- `pyproject.toml`;
- package installable ;
- dépendances ;
- structure `src/` lorsqu'elle devient utile ;
- relation entre packaging, environnement et gestionnaire de dépendances.

Ne pas transformer un petit script en package sans raison.

### 32. HTTP et API

À comprendre :

- HTTP;
- méthodes principales;
- codes de statut;
- JSON;
- REST;
- timeouts;
- validation des réponses;
- erreurs réseau.

Outils possibles lorsque nécessaires :

- `requests`;
- `httpx`.

Une réponse réseau est une entrée non fiable.

### 33. Persistance

À connaître :

- SQL de base;
- SQLite;
- transactions;
- paramètres SQL;
- notion d'ORM.

Un repository n'est utile que s'il apporte une vraie séparation entre métier et persistance.

### 34. Sécurité

Toujours considérer comme non fiables :

- entrées utilisateur;
- fichiers;
- variables d'environnement;
- réseau;
- API;
- base de données externe.

Principes :

- valider aux frontières;
- ne jamais mettre de secret dans le code;
- utiliser des requêtes SQL paramétrées;
- contrôler les chemins de fichiers;
- gérer explicitement les erreurs;
- ne jamais exposer d'information sensible dans les logs.

## Priorités théoriques

Ordre recommandé pour consolider les bases :

1. mutabilité et immutabilité;
2. références et copies;
3. portée des variables;
4. fonctions et responsabilités;
5. exceptions;
6. modules et packages;
7. itérables, itérateurs et générateurs;
8. POO et composition;
9. typing;
10. tests;
11. complexité Big-O;
12. architecture et séparation des responsabilités.

La théorie doit toujours rester liée à un exercice, une explication ou un projet concret.

## Passer de la théorie au projet

Utiliser [la table des projets](../projects/README.md#parcours-et-références) pour retrouver une pratique liée à chaque sujet. Le [parcours inventaire](../projects/maker-inventory.md) relie ses fonctionnalités aux sections de cette fiche et aux étapes de roadmap.

Pour une notion sans besoin immédiat dans le projet, proposer un exercice ciblé au moment adapté ; ne pas ajouter de fonctionnalité artificielle.
