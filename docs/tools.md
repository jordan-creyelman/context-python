# Mode tools

Objectif : produire un script complet directement exploitable. Annoncer `Mode : tools`. Clarifier uniquement les informations qui changent réellement le comportement (format, entrée/sortie, écrasement, plateforme). Pour les détails mineurs, choisir une option simple et expliciter l'hypothèse.

## Livraison

- Besoin et hypothèses en quelques lignes.
- Script complet, sans TODO ni partie laissée en exercice, avec main(), garde d'entrée, annotations et docstrings utiles.
- Arguments documentés, entrées validées, erreurs attendues traitées, codes de sortie cohérents.
- Résultats sur stdout et logging utile sur stderr ; ne pas journaliser de mots de passe ou contenu sensible.
- Commandes exactes d'utilisation, exemple de sortie, version Python et dépendances.
- Tests essentiels exécutés : succès, cas limites, entrée invalide et échec opérationnel pertinents. Rapporter le résultat réel et les limites de vérification.

Séparer une fonction métier testable de la CLI suffit souvent. Utiliser unittest et des dossiers temporaires pour garder le dépôt sans dépendances. Vérifier aussi l'interface réelle et son code de sortie. Les types documentent les interfaces ; ils ne remplacent ni validation ni tests.

Pour les opérations d'écriture, préciser ce qui sera créé/modifié, protéger les données existantes et tester dans un dossier isolé. Pour le réseau, définir un délai et traiter les erreurs si le besoin exige du réseau. Ne pas ajouter réseau, configuration, packaging ou classes par anticipation.

Le [compteur de journal](../projects/log_summary.py) est une référence minimale : CLI, lecture UTF-8, gestion d'erreurs, logging et tests. Une explication pédagogique peut suivre, mais ne remplace jamais la livraison complète.
