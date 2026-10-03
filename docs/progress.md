# Progression Python

Repère de reprise. Cocher uniquement après validation réelle ; ajouter une date et une preuve courte lorsque c'est utile.

## Acquis validés

- [x] Exécution, print, variables, chaînes
- [ ] Nombres, conversions, input
- [x] Conditions et booléens
- [x] Listes, dictionnaires et boucles
- [x] Fonctions, paramètres et return
- [ ] Compréhensions, itérateurs et générateurs
- [ ] pathlib, with et UTF-8
- [ ] Context managers
- [ ] Exceptions et validation
- [ ] argparse, main, codes de sortie et logging
- [ ] Types, docstrings et unittest
- [ ] Modules, imports et packages simples
- [ ] Fonctions avancées et décorateurs
- [ ] Classes, attributs et méthodes
- [ ] dataclasses
- [ ] Encapsulation, composition, héritage et polymorphisme
- [ ] Duck typing et Protocol
- [ ] Mini-projet complet
- [ ] Architecture simple et dépendances
- [ ] Design patterns essentiels
- [ ] Packaging et pyproject.toml
- [ ] Profiling et performance
- [ ] asyncio lorsque le besoin est compris

## Preuves et projets réalisés

- 2026-10-03 — Exécution, print, variables, chaînes : utilisation répétée de variables et affichages dans les exercices d'inventaire Python.
- 2026-10-03 — Conditions et booléens : utilisation correcte de conditions pour déterminer un statut de stock.
- 2026-10-03 — Listes, dictionnaires et boucles : création et parcours d'une liste de dictionnaires représentant des composants.
- 2026-10-03 — Fonctions, paramètres et return : création et utilisation de `show_component(component)` et `get_stock_status(component)`, avec distinction entre calcul retourné et affichage.
- 2026-10-03 — Recherche d'inventaire : utilisation correcte de `found = False` / `found = True`, gestion du cas `Component not found` et recherche insensible à la casse avec `.lower()`.
- 2026-10-03 — Compréhensions de liste : première utilisation correcte pour extraire les noms des composants ; notion encore en cours car itérateurs et générateurs ne sont pas encore étudiés.

## Repère pour la prochaine séance

- Dernier exercice : compréhension de liste pour extraire et filtrer les noms de composants.
- État : en cours.
- Résultat observé : création correcte de `component_names = [component["name"] for component in components]` et affichage avec `", ".join(component_names)`.
- Difficulté rencontrée : aucune bloquante sur la compréhension simple ; la compréhension avec condition est en cours.
- Prochaine étape proposée : terminer la compréhension avec condition, puis introduire itérateurs et générateurs avant de valider l'étape 6.

## Points à revoir

- Placement de `input()` par rapport à une boucle.
- Arrêt ou poursuite d'une boucle après avoir trouvé un élément.
- Différence entre une boucle classique et une compréhension de liste.
