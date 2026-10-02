# Mini-projets et scripts

Choisir un projet adapté aux acquis en learning ; fournir l'outil complet en tools. Commencer par le besoin minimum et ajouter seulement les améliorations utiles.

## Compteur de journal — référence tools fournie

[log_summary.py](log_summary.py) lit un fichier UTF-8 sans le modifier et compte les lignes qui commencent exactement par `ERROR ` (sensible à la casse). `INFO ERROR` et `ERROR` sans espace ne comptent pas. Lecture ligne par ligne, mémoire limitée à la taille d'une ligne ; fichier stable attendu pendant l'exécution.

```bash
python3 projects/log_summary.py "my folder/app.log"
python3 projects/log_summary.py "my folder/app.log" --verbose
python3 -m unittest discover -s tests -v
```

Pour un fichier contenant `ERROR failed`, `INFO ready`, `ERROR timeout` sur trois lignes, stdout vaut `2`. --verbose ajoute un diagnostic INFO sur stderr. Fichier vide ou sans erreur : `0`, code 0. Fichier absent, dossier ou encodage invalide : diagnostic, aucun total, code 1. Argument absent : aide d'usage, code 2. Python 3.11+, aucune dépendance externe ; exécution vérifiée uniquement sur la plateforme annoncée dans le compte rendu.

Prérequis learning : fichiers, fonctions et exceptions ; puis CLI, types, docstrings, logging et tests. Lire cet exemple complet à cette étape ou sur demande de correction, pas comme solution imposée au premier exercice.

## Rapport disque — projet à construire

Utiliser shutil.disk_usage sur un dossier donné, afficher total/utilisé/libre, gérer chemin absent et erreurs système. Prérequis : fonctions, chemins, CLI. Tests : dossier temporaire, chemin avec espaces, entrée invalide ; ne pas supposer une taille disque fixe.

## Sauvegarde ciblée — projet à construire

Archiver un dossier fictif avec tarfile, destination hors source, refus d'écraser une archive existante, simulation pertinente. Prérequis : validations, exceptions et effets sur fichiers. Tester source absente, destination invalide, espaces et archive existante ; vérifier le contenu et restaurer dans un dossier isolé. Ne pas extraire une archive non fiable pour tester.

## Projet terminé

Usage clair, main() et garde d'entrée, code anglais lisible, annotations et docstrings utiles, entrées validées, erreurs/logging sur stderr, codes documentés, tests essentiels exécutés et résultats réels annoncés. Pas de framework, CI ni dépendance anticipée.
