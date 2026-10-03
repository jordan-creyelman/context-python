# Débogage et diagnostic

Pourquoi : trouver la cause d'un problème avant de modifier le code.

## Méthode

1. **Symptôme** : noter entrée, sortie attendue, sortie réelle et message exact.
2. **Reproduction minimale** : réduire les données et conserver le problème.
3. **Hypothèse** : proposer une seule cause vérifiable.
4. **Test** : observer la valeur, le type ou le chemin d'exécution concerné.
5. **Correction minimale** : corriger la cause.
6. **Vérification** : refaire le cas initial et un cas proche.
7. **Non-régression** : ajouter un test utile lorsque les tests ont été étudiés.

## Exemple dans l'inventaire

Symptôme : `esp32` ne trouve pas le composant `ESP32`.

Hypothèse : la comparaison tient compte de la casse.

Test : comparer les deux chaînes avant et après `.lower()`.

Correction : normaliser les deux côtés de la recherche.

Vérification : essayer un nom existant, une casse différente et un nom absent.

## Outils progressifs

- Lire le traceback jusqu'au type d'exception et à la ligne de son propre code.
- Utiliser temporairement `print(repr(value), type(value))` pour une observation ciblée.
- Étudier `breakpoint()` pour inspecter un état et avancer pas à pas.
- Utiliser le logging pour les diagnostics durables après son introduction.
- Retirer les traces temporaires avant le commit ; ne jamais afficher un secret.

## Note de diagnostic

- Entrée minimale :
- Résultat attendu :
- Résultat réel :
- Hypothèse :
- Observation :
- Correction :
- Vérification exécutée :

Voir aussi [les erreurs classiques](anti-patterns.md).
