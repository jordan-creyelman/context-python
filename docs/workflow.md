# Workflow professionnel progressif

Pourquoi : rendre une modification compréhensible, vérifiable et facile à reprendre.

Appliquer ce workflow aux projets d'apprentissage selon les notions déjà étudiées. Git ne doit pas bloquer la découverte de Python.

## Boucle de travail

1. Définir un besoin court et un résultat observable dans une issue ou une note.
2. Lire le code existant et choisir la plus petite modification utile.
3. Créer une branche pour une fonctionnalité ou une correction.
4. Implémenter une petite étape ; vérifier son comportement.
5. Relire le diff, retirer les fichiers temporaires et vérifier l'absence de secrets.
6. Faire un commit explicite ; ouvrir une PR lorsque la collaboration le justifie.
7. Relire la PR : besoin, comportement, erreurs et vérifications réellement exécutées.

Exemple de commandes, dans le dépôt du projet :

```bash
git status
git switch -c feat/inventory-search
git diff
git add maker_inventory.py
git diff --cached
git commit -m "feat: add case-insensitive inventory search"
```

Adapter les chemins aux fichiers réellement modifiés. Éviter les commits contenant plusieurs sujets sans rapport.

## README du projet

Décrire le besoin, la version de Python, l'installation, un exemple d'exécution, les tests et les limites connues. Documenter uniquement les dépendances réellement utilisées.

## Environnement et outils

- Étudier un environnement virtuel lorsqu'une dépendance externe apparaît.
- Ignorer les environnements, caches et fichiers locaux sensibles avec `.gitignore`.
- Ne jamais versionner un secret ; utiliser une configuration externe adaptée.
- Introduire lint, typage statique et CI après avoir compris les vérifications locales.
- Avant une mise à jour de progression, appliquer les critères de [progress.md](progress.md).

Pour la clôture, utiliser [la checklist](../checklists/project-completion.md).
