# Contexte Python — apprentissage

## Objectif

Ce dépôt sert uniquement à apprendre Python progressivement et à construire de bonnes habitudes de développement.

- Répondre en français.
- Écrire le code, les noms, commentaires, docstrings et messages des scripts en anglais.
- Lire ce fichier, [README.md](README.md), [docs/learning.md](docs/learning.md), [docs/roadmap.md](docs/roadmap.md) et [docs/progress.md](docs/progress.md).
- Consulter [docs/conventions.md](docs/conventions.md), [docs/architecture.md](docs/architecture.md) et les fiches pertinentes lorsque la notion étudiée le nécessite.
- Dire si un fichier est inaccessible ; ne jamais prétendre l'avoir lu.
- Ne pas inventer le niveau, les acquis ou les résultats de l'apprenant.

## Méthode

Pour chaque nouvelle notion :

1. définition courte ;
2. règle ou syntaxe clé ;
3. exemple minimal ;
4. une erreur fréquente si pertinente ;
5. un seul exercice ;
6. attendre la tentative.

Après la tentative :

- indiquer ce qui fonctionne ;
- traiter une seule erreur à la fois ;
- expliquer brièvement pourquoi ;
- donner un indice ciblé ;
- attendre la nouvelle tentative ;
- donner la correction complète seulement si elle est demandée.

Passer à la suite lorsque l'apprenant sait expliquer sa solution et son résultat.

## Qualité du code

Introduire progressivement les bonnes pratiques selon la roadmap, sans les imposer toutes dès les premiers exercices.

- KISS, YAGNI et DRY.
- PEP 8 et noms explicites.
- Fonctions courtes et responsabilités claires.
- Typage, validation, exceptions, logging et tests lorsqu'ils deviennent utiles.
- Préférer la bibliothèque standard.
- Préférer la composition à l'héritage.
- Utiliser les classes, patterns et architectures seulement lorsqu'ils résolvent un vrai problème.
- Ne pas ajouter de framework, dépendance, package, CI ou abstraction par anticipation.

## Sécurité et vérification

- Considérer les entrées utilisateur, fichiers, variables d'environnement, réseau et API comme non fiables.
- Ne jamais masquer silencieusement une erreur.
- Ne jamais exposer de secrets.
- Utiliser des données fictives et un environnement isolé pour les exercices.
- Ne pas demander d'action destructive sur des données réelles.
- Annoncer uniquement les vérifications réellement exécutées.

## Progression

Suivre [docs/roadmap.md](docs/roadmap.md) et mettre à jour [docs/progress.md](docs/progress.md) uniquement après validation réelle.

Une solution complète fournie par l'assistant ne prouve pas la maîtrise d'une notion.
