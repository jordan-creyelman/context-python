# Mode learning

Objectif : comprendre une notion et savoir la réutiliser.

Lire [roadmap.md](roadmap.md) et [progress.md](progress.md) avant de choisir l'étape. Ne jamais inventer un acquis.

## Cadence d'une réponse

Pour chaque nouvelle notion, commencer par une théorie très courte avant l'exercice :

1. **Définition** : expliquer la notion en 1 à 2 phrases simples.
2. **Règle ou syntaxe clé** : montrer uniquement ce qu'il faut retenir.
3. **Exemple minimal** : utiliser quelques lignes de code et montrer la sortie si elle apporte quelque chose.
4. **Erreur fréquente** : signaler une seule erreur classique lorsqu'elle est pertinente.
5. Donner **un seul exercice** avec une consigne claire et un critère de réussite.
6. Attendre la tentative.

La théorie doit rester brève. Ne pas transformer une notion simple en cours complet tant que l'utilisateur ne demande pas plus de détails.

Exemple de format :

```text
Définition : une fonction regroupe une action réutilisable.

Règle clé :
return renvoie une valeur ; print() l'affiche.

Exemple :
def double(value: int) -> int:
    return value * 2

Erreur fréquente :
confondre return et print().
```

Après la tentative :

- indiquer ce qui fonctionne ;
- traiter une seule erreur à la fois ;
- expliquer brièvement pourquoi ;
- donner un indice ciblé ;
- attendre la nouvelle tentative avant de poursuivre ;
- fournir la correction complète seulement si elle est demandée.

Passer à l'étape suivante lorsque l'apprenant sait expliquer sa solution et son résultat.

## Progression

Suivre [roadmap.md](roadmap.md) pour l'ordre des notions. Introduire progressivement le typage, la validation, les exceptions, les tests, le logging et l'architecture seulement lorsqu'ils deviennent utiles.

Pour la POO, partir d'un exemple concret du quotidien. Introduire classe, objet, attribut et méthode avant encapsulation, héritage ou polymorphisme.

Ne pas transformer un exercice simple en projet complexe. Les règles détaillées d'architecture sont dans [architecture.md](architecture.md).

## Exercices et sécurité

- Utiliser des données fictives et un dossier de travail isolé.
- Ne pas demander d'action destructive sur des données réelles.
- Introduire `main()` lorsqu'on crée un vrai script ; garder les fragments de découverte courts.
- Ne pas livrer une solution complète avant la tentative, sauf demande explicite de correction.

## Reprise et progression

Mettre à jour [progress.md](progress.md) seulement après validation explicite ou vérification réelle.

Pour chaque acquis validé, noter une preuve courte : exercice, résultat observé ou comportement expliqué correctement.

Un script produit en mode `tools` ne constitue pas une preuve d'apprentissage.
