# Mode tools

Objectif : produire un script complet directement exploitable.

Annoncer `Mode : tools`. Clarifier uniquement les informations qui changent réellement le comportement ; pour les détails mineurs, choisir une hypothèse simple et l'indiquer.

Les règles générales de style, typage, validation, erreurs, logging et tests sont centralisées dans [conventions.md](conventions.md). Les choix de structure sont détaillés dans [architecture.md](architecture.md).

## Dépendances

Préférer la bibliothèque standard.

Si une bibliothèque externe est réellement nécessaire :

- expliquer pourquoi ;
- utiliser un environnement virtuel ;
- fournir la commande d'installation exacte ;
- ne pas installer globalement ;
- ne pas créer de fichier de dépendances sans besoin réel.

## Livraison attendue

Une réponse `tools` doit fournir, lorsque pertinent :

- le besoin et les hypothèses ;
- les fichiers créés ou modifiés ;
- un script complet sans TODO ;
- `main()` et une garde d'entrée pour une CLI ;
- des annotations de types et docstrings utiles ;
- des entrées validées et des erreurs explicites ;
- des codes de sortie cohérents ;
- des résultats sur stdout et diagnostics sur stderr ;
- les commandes exactes d'utilisation ;
- la version Python et les dépendances ;
- les tests essentiels ;
- les résultats de vérification réellement observés.

Après correction d'un bug, ajouter un test de non-régression lorsque cela apporte une vraie valeur.

## Architecture

Commencer par la structure minimale. Extraire des modules seulement lorsque cela clarifie une responsabilité ou améliore les tests.

Pour les choix plus avancés (`src/`, Clean Architecture, DDD), suivre [architecture.md](architecture.md) et ne les introduire que si le projet le justifie réellement.

## Opérations sensibles

Pour les écritures ou suppressions :

- protéger les données existantes ;
- refuser l'écrasement par défaut lorsque pertinent ;
- proposer une simulation pour les actions risquées ou massives ;
- tester dans un environnement isolé.

Pour le réseau, définir un délai et traiter les erreurs lorsque le besoin exige du réseau.

## Référence

Le [compteur de journal](../projects/log_summary.py) montre une implémentation minimale : CLI, lecture UTF-8, erreurs explicites, logging, codes de sortie et tests.
