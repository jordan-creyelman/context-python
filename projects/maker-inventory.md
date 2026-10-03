# Projet — Inventaire maker

Pourquoi : gérer des composants tout en faisant progresser naturellement les notions Python.

Cette fiche décrit un parcours, pas une solution complète. Reprendre l'étape indiquée dans [la progression](../docs/progress.md) et présenter une seule fonctionnalité à la fois.

## Besoin

Afficher et rechercher des composants fictifs avec un nom, une catégorie et une quantité. Ajouter ensuite la persistance et les vérifications lorsque les prérequis sont acquis.

## Liens entre besoin, théorie et roadmap

| Fonctionnalité | Étapes de roadmap | Théorie |
| --- | --- | --- |
| Afficher les composants et leur stock | 1–5 | [Collections](../docs/theory.md#2-collections), [fonctions](../docs/theory.md#4-fonctions-et-portée) |
| Extraire et filtrer les noms | 6 | [Compréhensions](../docs/theory.md#5-compréhensions) |
| Parcourir progressivement des données | 6 | [Itérateurs](../docs/theory.md#15-itérables-et-itérateurs), [générateurs](../docs/theory.md#16-générateurs) |
| Charger et sauvegarder du JSON | 7–9 | [Fichiers](../docs/theory.md#9-fichiers-et-données), [exceptions](../docs/theory.md#7-exceptions) |
| Ajouter une CLI si nécessaire | 10 | [Conventions CLI](../docs/conventions.md#entrées-et-validation) |
| Documenter les contrats et vérifier la recherche | 11 | [Typage](../docs/theory.md#10-typage), [tests](../docs/testing.md) |
| Extraire métier et stockage si nécessaire | 12, 19 | [Architecture](../docs/architecture.md) |

Un générateur n'est pas nécessaire pour trois composants : l'étudier sur un jeu de données adapté pour comprendre son intérêt.

## Critères observables

- La recherche reconnaît le nom indépendamment de la casse.
- Un nom absent et une collection vide sont gérés.
- La règle de stock est explicable, y compris au seuil.
- Un fichier invalide produit une erreur utile lorsque la persistance est ajoutée.
- La logique métier devient testable indépendamment du terminal lorsque les tests sont étudiés.

## Fin d'étape

Noter la fonctionnalité réalisée, la sortie observée, la notion pratiquée et la prochaine étape dans [progress.md](../docs/progress.md). Utiliser [la checklist](../checklists/project-completion.md) en fin de projet.
