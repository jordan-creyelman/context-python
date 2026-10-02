# Mémo Python

Consulter seulement les notions utiles à l'étape actuelle.

```python
name = "Ada"                  # str
count = 3                     # int
ratio = 0.5                   # float
ready = True                  # bool
print(f"Hello, {name}!")

if count > 0:
    print("Items available")

hosts = ["alpha", "beta"]
for host in hosts:
    print(host)

machine = {"name": "alpha", "active": True}
print(machine["name"])


def double(value: int) -> int:
    """Return twice the given value."""
    return value * 2
```

`=` affecte une valeur ; `==` compare. L'indentation délimite les blocs. input() retourne une chaîne ; int() convertit et peut lever ValueError. Une liste vide est fausse dans une condition. return donne un résultat à l'appelant ; print l'affiche.

## Exemple POO du quotidien

```python
class Book:
    """Represent a book that can be borrowed."""

    def __init__(self, title: str) -> None:
        self.title = title
        self.borrowed = False

    def borrow(self) -> None:
        self.borrowed = True


book = Book("Python basics")
book.borrow()
print(book.title, book.borrowed)
```

Sortie : `Python basics True`. Book est la classe, book un objet, title et borrowed des attributs, borrow une méthode. Pas d'attribut privé nécessaire ici. Voir la feuille de route avant d'ajouter héritage ou polymorphisme.
