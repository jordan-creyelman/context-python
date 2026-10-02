# Fichiers et ligne de commande

## Lire un fichier texte

```python
from pathlib import Path

path = Path("my folder/app.log")
try:
    with path.open(encoding="utf-8") as stream:
        for line in stream:
            print(line.rstrip("\n"))
except (OSError, UnicodeError) as error:
    print(f"Cannot read file: {error}")
```

Petit fragment pédagogique ; dans un outil, envoyer le diagnostic via logging sur stderr et retourner un code non nul. pathlib gère le chemin comme une valeur. Dans le terminal, entourer un chemin avec espaces de guillemets.

## Arguments et diagnostics

```python
import argparse
import logging
from pathlib import Path

parser = argparse.ArgumentParser(description="Read a UTF-8 log.")
parser.add_argument("log_file", type=Path)
parser.add_argument("--verbose", action="store_true")
args = parser.parse_args()
logging.basicConfig(
    level=logging.INFO if args.verbose else logging.WARNING,
    format="%(levelname)s: %(message)s",
)
```

Placer cette configuration dans main() pour un script complet. argparse génère --help et retourne le code 2 si un argument obligatoire manque. Le type Path ne prouve ni l'existence ni la lisibilité du fichier.

## Tests sans dépendance

`python3 -m unittest discover -s tests -v` découvre les fichiers test_*.py. Utiliser tempfile.TemporaryDirectory pour isoler les fichiers. Le [script complet](../projects/log_summary.py) et ses [tests](../tests/test_log_summary.py) montrent la séparation logique/CLI.
