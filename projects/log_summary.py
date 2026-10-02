#!/usr/bin/env python3
"""Count lines starting with 'ERROR ' in a UTF-8 file without modifying it."""

import argparse
import logging
from pathlib import Path
from typing import Sequence

LOGGER = logging.getLogger(__name__)


def count_errors(log_file: Path) -> int:
    """Return the matching line count; propagate file and decoding errors."""
    with log_file.open(encoding="utf-8") as stream:
        return sum(1 for line in stream if line.startswith("ERROR "))


def main(argv: Sequence[str] | None = None) -> int:
    """Run the CLI: return 0 on success or 1 on read failure; argparse exits 2."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("log_file", type=Path, help="UTF-8 log file to read")
    parser.add_argument("--verbose", action="store_true", help="Show read diagnostics")
    args = parser.parse_args(argv)
    logging.basicConfig(
        level=logging.INFO if args.verbose else logging.WARNING,
        format="%(levelname)s: %(message)s",
    )

    try:
        if not args.log_file.is_file():
            LOGGER.error("Expected an existing regular file: %s", args.log_file)
            return 1
        total = count_errors(args.log_file)
    except (OSError, UnicodeError) as error:
        LOGGER.error("Cannot read %s: %s", args.log_file, error)
        return 1

    LOGGER.info("Read %s; found %d ERROR lines", args.log_file, total)
    print(total)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
