# Erreurs classiques

Pourquoi : reconnaître les erreurs fréquentes sans introduire des règles abstraites.

| Erreur | Conséquence | Habitude utile |
| --- | --- | --- |
| Confondre `print()` et `return` | Le résultat ne peut pas être réutilisé | Retourner le calcul, afficher dans l'interface |
| Utiliser `is` pour comparer des chaînes | Comparaison d'identité au lieu de valeur | Utiliser `==` ; réserver `is None` au test de `None` |
| Paramètre par défaut mutable | État partagé entre appels | Utiliser `None` puis créer la collection |
| Modifier une liste pendant son parcours | Éléments sautés ou résultat difficile à prévoir | Produire une nouvelle collection si adapté |
| Compréhension trop complexe | Lecture et diagnostic difficiles | Utiliser une boucle claire |
| `except Exception: pass` | Erreur cachée et faux succès | Capturer une exception précise et traiter l'échec |
| Croire que les annotations valident les données | Entrées invalides acceptées | Valider aux frontières |
| Saisie, stockage et métier dans une seule fonction | Tests difficiles | Séparer les responsabilités progressivement |
| Code exécuté lors d'un import | Effets de bord inattendus | Utiliser une garde d'entrée |
| Classe ou pattern sans besoin | Complexité supplémentaire | Préférer une fonction ou une structure native |
| Tests qui copient l'implémentation | Même erreur dans le test et le code | Vérifier le contrat observable |
| Optimiser sans mesure | Effort sans bénéfice démontré | Mesurer un problème réel avant d'optimiser |

Étudier une seule erreur pertinente à la fois. Utiliser [la méthode de diagnostic](debugging.md) pour comprendre sa cause.
