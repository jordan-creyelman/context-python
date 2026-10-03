# Mode tools

Objectif : produire un script complet directement exploitable. Annoncer `Mode : tools`. Clarifier uniquement les informations qui changent réellement le comportement (format, entrée/sortie, écrasement, plateforme). Pour les détails mineurs, choisir une option simple et expliciter l'hypothèse.

## Dépendances

Privilégier la bibliothèque standard. Si une bibliothèque externe est nécessaire au besoin, expliquer pourquoi et fournir les commandes exactes pour créer un environnement virtuel et y installer les dépendances. Sur Linux/macOS : `python3 -m venv .venv`, puis `.venv/bin/python -m pip install NOM_DU_PAQUET` (remplacer par le vrai nom). Sur Windows : `py -3 -m venv .venv`, puis `.venv\Scripts\python.exe -m pip install NOM_DU_PAQUET`. Indiquer ensuite comment lancer le script avec ce même interpréteur. Ne pas installer globalement ou créer un requirements.txt sans besoin réel. Les scripts fournis ici restent sans dépendance externe.

## Typage

- Annoter les paramètres et retours des fonctions importantes.
- Préférer la syntaxe Python 3.11+ : `list[str]`, `dict[str, int]`, `str | None`.
- Éviter `Any` sauf nécessité réelle.
- Ne pas surcharger le code avec des annotations locales évidentes.
- Le typage documente le contrat ; il ne remplace pas la validation à l'exécution.
- Si mypy ou pyright est déjà configuré dans le projet, l'exécuter après modification. Ne pas ajouter l'outil uniquement par habitude.

## Gestion d'erreurs

- Valider les entrées utilisateur, fichiers, variables d'environnement, données réseau et API aux frontières du programme.
- Utiliser des exceptions précises pour les erreurs attendues.
- Ne jamais masquer une exception avec `except Exception: pass`.
- Transformer une erreur en message utilisateur seulement à la frontière CLI ; garder la logique métier testable.
- Utiliser logging pour les diagnostics techniques utiles, jamais pour exposer des secrets.
- Retourner un code de sortie cohérent pour les scripts CLI.
- Ne jamais utiliser une valeur de retour ambiguë pour faire croire qu'une opération a réussi.

## Tests

Ajouter les tests utiles, sans viser une couverture artificielle.

Priorité :
1. cas nominal ;
2. cas limite pertinent ;
3. entrée invalide ;
4. erreur importante ;
5. test de non-régression après correction d'un bug.

Privilégier les tests unitaires rapides pour la logique isolée. Ajouter des tests d'intégration uniquement lorsqu'ils valident une interaction réelle utile. Pour une CLI, tester les arguments, stdout/stderr et codes de sortie lorsque pertinent.

Utiliser `unittest` et des dossiers temporaires par défaut afin de ne pas ajouter de dépendance. Utiliser pytest seulement si le projet l'utilise déjà ou si son apport est justifié.

## Livraison

- Besoin et hypothèses en quelques lignes.
- Script complet, sans TODO ni partie laissée en exercice, avec main(), garde d'entrée, annotations et docstrings utiles.
- Arguments documentés, entrées validées, erreurs attendues traitées, codes de sortie cohérents.
- Résultats sur stdout et logging utile sur stderr ; ne pas journaliser de mots de passe ou contenu sensible.
- Commandes exactes d'utilisation, exemple de sortie, version Python et dépendances.
- Tests essentiels exécutés : succès, cas limites, entrée invalide et échec opérationnel pertinents.
- Après correction d'un bug, ajouter un test de non-régression lorsqu'il est pertinent.
- Rapporter les résultats réellement observés et les limites de vérification.

Séparer une fonction métier testable de la CLI suffit souvent. Les types documentent les interfaces ; ils ne remplacent ni validation ni tests.

Pour les opérations d'écriture, préciser ce qui sera créé/modifié, protéger les données existantes et tester dans un dossier isolé. Pour le réseau, définir un délai et traiter les erreurs si le besoin exige du réseau. Ne pas ajouter réseau, configuration, packaging ou classes par anticipation.

Le [compteur de journal](../projects/log_summary.py) est une référence minimale : CLI, lecture UTF-8, gestion d'erreurs, logging et tests. Une explication pédagogique peut suivre, mais ne remplace jamais la livraison complète.
