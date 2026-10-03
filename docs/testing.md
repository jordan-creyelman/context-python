# Tests utiles

Pourquoi : vérifier un comportement et détecter sa régression lorsque le code évolue.

Les conventions communes restent dans [conventions.md](conventions.md). Cette fiche explique comment choisir et écrire les tests à l'étape 11 de [la roadmap](roadmap.md).

## Choisir les cas

Pour une recherche d'inventaire :

| Cas | Résultat attendu |
| --- | --- |
| Nom existant | Composant correspondant |
| Casse différente | Même composant |
| Nom absent | Résultat d'absence prévu par le contrat |
| Collection vide | Absence sans crash |

Ne pas inventer une politique de doublons ou de saisie vide : la définir avant de la tester.

## Arrange / Act / Assert

Préparer les données → appeler la fonction → vérifier le résultat.

Exemple indépendant :

```python
"""Test a stock threshold rule."""

import unittest


def is_low_stock(quantity: int, threshold: int) -> bool:
    """Return whether quantity is below the threshold."""
    return quantity < threshold


class LowStockTests(unittest.TestCase):
    """Check behavior at the stock threshold."""

    def test_quantity_at_threshold_is_not_low(self) -> None:
        """Keep the threshold itself outside low stock."""
        quantity = 5
        result = is_low_stock(quantity, threshold=5)
        self.assertFalse(result)
```

Le cas au seuil détecte une erreur utile entre `<` et `<=`. Dans un vrai projet, importer la fonction du module métier plutôt que recopier sa définition dans le test.

## Isolation

- Tester d'abord les fonctions métier sans saisie au clavier ni réseau.
- Utiliser `tempfile.TemporaryDirectory` pour les fichiers.
- Tester les erreurs attendues avec `assertRaises`.
- Ajouter une intégration si l'interaction CLI / fichier ou stockage apporte une preuve utile.
- Utiliser un mock seulement pour une dépendance externe à isoler ; ne pas reproduire toute l'implémentation.

## Vérification

Dans un projet possédant un dossier `tests/` :

```bash
python3 -m unittest discover -s tests -v
```

Un test qui passe ne prouve ni la maîtrise de l'apprenant ni la qualité de tous les cas possibles. Noter le comportement réellement vérifié.
