"""Utility to determine whether numbers are prime.

Running this module directly provides both a command-line interface and an
interactive prompt as a fallback. This makes it easier to use on systems such
as Windows where the Python executable might need to be quoted when invoked via
PowerShell.
"""

from __future__ import annotations

import argparse
import math
from typing import Optional


def is_prime(n: int) -> bool:
    """Return True if ``n`` is a prime number, otherwise False.

    Negative numbers, 0, and 1 are not prime. Uses trial division up to the
    square root of ``n``.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = int(math.isqrt(n))
    for divisor in range(3, limit + 1, 2):
        if n % divisor == 0:
            return False
    return True


def parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
    """Return parsed command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Check whether a number is prime.",
        epilog=(
            "If no number is provided on the command line, an interactive "
            "prompt will ask for one. On Windows PowerShell, use quotes with "
            "the call operator (&) when paths contain spaces or non-ASCII "
            "characters, for example: "
            '"& \"C:/Path With Spaces/python.exe\" \"prime_checker.py\" 11".'
        ),
    )
    parser.add_argument(
        "number",
        type=int,
        nargs="?",
        help="An optional integer to check for primality.",
    )
    return parser.parse_args(argv)


def main() -> None:
    args = parse_args()

    if args.number is not None:
        value = args.number
    else:
        try:
            value = int(input("Enter an integer: "))
        except ValueError:
            print("Please enter a valid integer.")
            return

    if is_prime(value):
        print(f"{value} is a prime number.")
    else:
        print(f"{value} is not a prime number.")


if __name__ == "__main__":
    main()
