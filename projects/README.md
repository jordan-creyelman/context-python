# Mini-projets d'apprentissage

Les mini-projets servent à combiner plusieurs notions déjà étudiées. Choisir un projet adapté aux acquis validés et construire la solution progressivement.

## Compteur de journal — projet de référence

[log_summary.py](log_summary.py) lit un fichier UTF-8 sans le modifier et compte les lignes qui commencent exactement par `ERROR `.

Il permet d'étudier progressivement :

- fonctions ;
- pathlib et fichiers ;
- exceptions ;
- argparse ;
- typage ;
- logging ;
- codes de sortie ;
- tests unitaires.

```bash
python3 projects/log_summary.py "my folder/app.log"
python3 projects/log_summary.py "my folder/app.log" --verbose
python3 -m unittest discover -s tests -v
```

Ne pas présenter immédiatement le fichier complet comme solution à un débutant. L'étudier lorsque les prérequis correspondants sont acquis ou lorsqu'une correction complète est demandée.

## Rapport disque

Construire progressivement un script utilisant `shutil.disk_usage` sur un dossier donné.

Notions possibles : fonctions, chemins, validation, CLI et tests.

Ne pas supposer une taille disque fixe dans les tests.

## Sauvegarde ciblée

Construire progressivement une sauvegarde avec `tarfile`.

Objectifs pédagogiques :

- valider source et destination ;
- éviter l'écrasement accidentel ;
- comprendre les effets sur le système de fichiers ;
- tester avec des dossiers fictifs ;
- vérifier le contenu dans un environnement isolé.

Ne jamais utiliser de données réelles importantes pour l'exercice.


## Projets guidés par la roadmap

Les projets doivent être choisis pour faire apparaître naturellement plusieurs notions successives de la roadmap.

### Inventaire maker

Bon projet pour les étapes débutant → junior :

- listes, dictionnaires et boucles ;
- fonctions ;
- compréhensions ;
- recherche et filtrage ;
- fichiers JSON ;
- validation et exceptions ;
- typing et docstrings ;
- tests ;
- modules lorsque le fichier devient réellement trop grand.

### Analyseur de logs

Bon projet pour junior :

- pathlib et fichiers ;
- itérateurs et générateurs ;
- exceptions ;
- CLI avec argparse ;
- logging ;
- tests ;
- séparation entre logique métier et interface.

### Gestionnaire de sauvegardes

Bon projet pour junior → medium :

- validation des chemins ;
- erreurs système ;
- configuration ;
- modules ;
- architecture simple ;
- tests d'intégration utiles ;
- logging.

### Client API

Bon projet pour medium :

- HTTP et JSON ;
- validation des réponses ;
- exceptions réseau ;
- typing ;
- séparation client / métier ;
- tests avec dépendances externes isolées ;
- async uniquement si un besoin de concurrence I/O apparaît.

Un projet n'a pas besoin de couvrir toute la roadmap. Ne jamais ajouter une fonctionnalité artificielle uniquement pour introduire une notion avancée.

## Projet terminé

Un projet est considéré comme maîtrisé lorsque l'apprenant peut expliquer :

- son besoin ;
- le rôle de ses fonctions ou modules ;
- ses entrées et sorties ;
- ses erreurs principales ;
- les tests importants ;
- les choix de structure réalisés.

La complexité doit rester proportionnelle au problème.

## Parcours et références

| Projet | Étapes principales | Références théoriques |
| --- | --- | --- |
| [Inventaire maker](maker-inventory.md) | 1–12, puis 19 si utile | Collections, fonctions, compréhensions, fichiers, exceptions, typage, tests |
| Analyseur de logs | 5–12, puis 19 si utile | [Fichiers](../docs/theory.md#9-fichiers-et-données), [générateurs](../docs/theory.md#16-générateurs), [logging](../docs/theory.md#27-logging) |
| Rapport disque | 5, 7, 9–11 | [Fonctions](../docs/theory.md#4-fonctions-et-portée), [exceptions](../docs/theory.md#7-exceptions), [tests](../docs/testing.md) |
| Gestionnaire de sauvegardes | 7–12, 18–19 | [Fichiers](../docs/theory.md#9-fichiers-et-données), [architecture](../docs/architecture.md), [tests](../docs/testing.md) |
| Client API | Après les bases ; 9, 11–12, 19 ; 23 si utile | [HTTP](../docs/theory.md#31-http-et-api), [sécurité](../docs/theory.md#33-sécurité), [concurrence](../docs/theory.md#28-concurrence) |

Les numéros renvoient à [la roadmap](../docs/roadmap.md). Choisir la prochaine fonctionnalité selon [la progression réelle](../docs/progress.md), puis clôturer avec [la checklist](../checklists/project-completion.md).
