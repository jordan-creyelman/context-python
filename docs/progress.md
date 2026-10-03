# Progression Python

Repère de reprise. Cocher uniquement après validation réelle ; ajouter une date et une preuve courte lorsque c'est utile.

## Règle de maintenance automatique

Ce fichier est la **source de vérité de l'état d'apprentissage**. Il doit être mis à jour au fil des séances lorsque des preuves suffisantes sont observées, même si l'apprenant ne demande pas explicitement de modifier la progression.

- **TODO** : pas encore étudié.
- **Learning** : découverte ou pratique avec aide.
- **Practiced** : réussi au moins une fois, mais autonomie ou explication encore à confirmer.
- **Validated** : réutilisé correctement avec compréhension démontrée.

À chaque mise à jour :

1. préserver les acquis déjà établis ;
2. ajouter une preuve datée concise ;
3. actualiser le repère de reprise ;
4. choisir ensuite le prochain objectif non Validated de la roadmap ;
5. ne jamais valider sur la seule base d'une solution fournie par l'assistant.

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

## Statuts de travail

| Statut | Signification | Preuve attendue |
| --- | --- | --- |
| TODO | Notion pas encore travaillée | Aucune |
| Learning | Découverte ou tentative avec aide | Étape en cours et difficulté |
| Practiced | Application réussie, autonomie à confirmer | Code ou résultat observé |
| Validated | Notion réutilisée et expliquée correctement | Preuve datée et critère de roadmap atteint |

Les cases cochées ci-dessus représentent les acquis Validated. Une case vide peut être TODO, Learning ou Practiced : elle ne signifie pas automatiquement « jamais étudié ». Ne pas reclasser les acquis existants sans preuve.

### Détail de l'étape 6

- Compréhension simple : **Practiced** — preuve du 2026-10-03 ci-dessus.
- Compréhension avec condition : **Learning** — exercice en cours.
- Itérateurs et générateurs : **TODO** — pas encore étudiés d'après le repère de reprise.

Une étape regroupant plusieurs notions reste non validée tant que ses critères ne sont pas remplis. Une fiche ajoutée par l'assistant ne change aucun statut à elle seule.
