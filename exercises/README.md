# Exercices progressifs — learning

Suivre [la feuille de route](../docs/roadmap.md) et le [mode learning](../docs/learning.md). Un seul exercice proposé à la fois, attente de la tentative, indices avant correction complète sauf demande explicite.

## Premier exercice : salutation

**Objectif :** comprendre variable et affichage. Une variable donne un nom à une valeur ; print affiche un résultat.

Petit exemple indépendant :

```python
city = "Brussels"
print(city)
```

Sortie : `Brussels`.

**Consigne :** dans un dossier de travail, créer greeting.py. Définir main(), y créer une variable name contenant un prénom fictif et afficher `Hello, <prénom>!`. Appeler main() sous la garde `if __name__ == "__main__":`.

**Exécution :** `python3 greeting.py`.

**Critères :** une seule salutation affichée ; changer name change le prénom affiché ; savoir distinguer le nom de la variable de sa valeur.

**À envoyer :** code et sortie observée. Attendre la tentative avant correction ou exercice suivant. Ne pas ajouter argparse, logging ou classes à ce premier exercice.

## Pour la suite

Créer un fichier exercises/02_topic.py seulement lorsqu'une activité le nécessite. Une notion principale, une consigne concrète, un exemple d'exécution et des critères observables. Utiliser des données fictives. Exécuter chaque script modifié si possible et expliquer les erreurs simplement. Pas de catalogue de solutions préparées.
