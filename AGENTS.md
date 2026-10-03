# Contexte Python — apprentissage et outils

## Rôle et langue

- Répondre en français ; code, noms, commentaires, docstrings et messages des scripts en anglais.
- Lire ce fichier et README.md, puis les fichiers spécialisés nécessaires au mode actif.
- Dire si un fichier est inaccessible ; ne jamais prétendre l'avoir lu.
- Ne pas supposer le niveau, le système, les outils installés ou les acquis.

## Choix du mode

- Respecter le mode explicite `learning` ou `tools` et l'annoncer brièvement.
- Apprendre, comprendre ou s'entraîner : `learning` → lire [docs/learning.md](docs/learning.md), [docs/roadmap.md](docs/roadmap.md) et [docs/progress.md](docs/progress.md).
- Demande de script ou outil directement utilisable : `tools` → lire [docs/tools.md](docs/tools.md).
- Si l'intention est ambiguë, demander le mode.
- Conserver le mode tant que l'utilisateur ne change pas d'objectif ou ne demande pas de bascule.
- Un résultat produit en `tools` ne valide pas automatiquement un acquis en `learning`.

## Règles communes

- Appliquer KISS, YAGNI et DRY.
- Respecter les [conventions Python](docs/conventions.md) pour le style, le typage, la validation, les erreurs, le logging et les tests.
- Suivre [l'architecture pragmatique](docs/architecture.md) uniquement lorsque la taille du projet la justifie.
- Préférer la bibliothèque standard et les solutions simples.
- Séparer logique métier, interface, stockage, réseau et infrastructure seulement lorsque ces responsabilités deviennent significatives.
- Préférer les fonctions simples ; utiliser des classes lorsqu'elles modélisent réellement un état et des comportements associés.
- Préférer la composition à l'héritage.
- Ne jamais ajouter de framework, package, CI, dépendance ou abstraction sans besoin concret.

## Sécurité et vérification

- Considérer les entrées utilisateur, fichiers, variables d'environnement, réseau et API comme non fiables.
- Ne jamais masquer une erreur silencieusement.
- Ne jamais exposer de secrets dans le code, les logs ou les exemples.
- Après modification d'un script, exécuter les vérifications pertinentes quand l'environnement le permet.
- Annoncer uniquement les contrôles réellement exécutés et leurs résultats.
- Pour une écriture ou suppression, protéger les données existantes et expliquer l'effet avant l'action lorsque nécessaire.

## Structure du dépôt

La structure de référence est décrite dans [README.md](README.md). Ajouter uniquement les fichiers réellement utiles.
