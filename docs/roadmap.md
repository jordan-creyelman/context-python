# Feuille de route Python

Un seul exercice présenté à la fois. Passer à l'étape suivante lorsque l'apprenant peut expliquer sa solution et son résultat ; adapter le départ aux acquis vérifiés.

| Étape | Notions | Mise en pratique | Critère de réussite |
| --- | --- | --- | --- |
| 1 | Exécution, print, variables, chaînes | Afficher un prénom | Modifier une variable et prédire la sortie |
| 2 | Nombres, conversions, input | Calculer une durée | Distinguer une chaîne d'un nombre |
| 3 | Conditions, booléens | Vérifier un seuil | Expliquer les deux branches |
| 4 | Listes, dictionnaires, boucles | Parcourir des machines fictives | Gérer une collection vide |
| 5 | Fonctions, paramètres, return | Extraire un calcul | Distinguer retour et affichage |
| 6 | Compréhensions, itérateurs, générateurs | Transformer ou parcourir une collection sans tout charger inutilement | Choisir une boucle, une compréhension ou un générateur selon le besoin |
| 7 | pathlib, with, UTF-8 | Lire un journal fictif | Gérer un chemin avec espaces et expliquer le rôle de with |
| 8 | Context managers | Encapsuler proprement ouverture et fermeture d'une ressource | Expliquer pourquoi une ressource doit être libérée même en cas d'erreur |
| 9 | Exceptions, validation | Refuser une entrée incorrecte | Expliquer l'échec avant de le traiter |
| 10 | argparse, main, codes de sortie, logging | Construire une CLI | Séparer résultats et diagnostics |
| 11 | Types, docstrings, unittest | Renforcer le script | Tester succès et erreurs utiles |
| 12 | Modules, imports, packages simples | Découper un script devenu trop grand | Importer sans effets de bord et expliquer la responsabilité de chaque module |
| 13 | Fonctions avancées et décorateurs | Ajouter un comportement transversal simple | Expliquer ce que le décorateur ajoute sans modifier la logique métier |
| 14 | Classes, attributs, méthodes | Livre et bibliothèque | Expliquer objet, état et comportement |
| 15 | dataclasses | Modéliser une donnée structurée simple | Préférer dataclass à une classe manuelle lorsque le besoin est surtout de stocker des données |
| 16 | Encapsulation, composition, héritage court, polymorphisme | Objets partageant une méthode | Préférer la composition et choisir l'héritage seulement s'il simplifie réellement le modèle |
| 17 | Duck typing et Protocol | Faire accepter plusieurs objets partageant un même contrat | Expliquer le contrat attendu sans imposer une hiérarchie de classes |
| 18 | Mini-projet adapté | Compteur de journal, inventaire ou rapport disque | Vérifier usage, limites, cas invalides et tests |
| 19 | Architecture simple et dépendances | Séparer métier, CLI, stockage et infrastructure | Justifier chaque séparation et garder des dépendances simples |
| 20 | Design patterns essentiels : Strategy, Factory, Adapter, Observer | Refactoriser un problème qui justifie réellement un pattern | Expliquer le problème résolu et éviter le pattern s'il ajoute plus de complexité qu'il n'en retire |
| 21 | Packaging et pyproject.toml | Transformer un projet multi-modules en package installable | Comprendre ce que le packaging apporte avant de l'ajouter |
| 22 | Profiling et performance | Mesurer un script avant optimisation | Identifier un vrai goulot d'étranglement avec une mesure plutôt qu'une intuition |
| 23 | asyncio, si le besoin apparaît | Exécuter plusieurs opérations d'E/S concurrentes | Expliquer quand async est utile et quand du code synchrone reste préférable |

Cadence : définition courte → règle ou syntaxe clé → exemple minimal → erreur fréquente si utile → un exercice → tentative → indice/correction → validation.

Les notions avancées viennent après une base solide. Les design patterns, le packaging, l'optimisation et asyncio ne sont pas des objectifs en soi : les introduire uniquement lorsqu'un problème concret les justifie.

En Python, préférer d'abord les fonctions, les structures natives, la composition et les outils de la bibliothèque standard lorsqu'ils suffisent. Ne pas introduire métaclasses, descriptors avancés, multiprocessing, framework ou déploiement avant un besoin réel. Les projets procéduraux n'exigent pas de POO.
