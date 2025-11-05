"""Command line utility to check if a number is prime."""

from __future__ import annotations

import argparse
import math
from typing import Optional


def is_prime(n: int) -> bool:
    """Return ``True`` if ``n`` is a prime number, otherwise ``False``.

    Negative numbers, ``0``, and ``1`` are not prime. The implementation uses
    trial division only up to the square root of ``n`` which is efficient for
    reasonably sized integers.
    """

    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = math.isqrt(n)
    for divisor in range(3, limit + 1, 2):
        if n % divisor == 0:
            return False
    return True


def parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
    """Parse command line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "number",
        nargs="?",
        type=int,
        help="Number to check for primality. If omitted, you will be prompted.",
    )
    return parser.parse_args(argv)


def prompt_for_number() -> Optional[int]:
    """Prompt the user for an integer, returning ``None`` if parsing fails."""

    try:
        return int(input("Enter an integer: "))
    except ValueError:
        return None


def main(argv: Optional[list[str]] = None) -> None:
    args = parse_args(argv)

    value = args.number if args.number is not None else prompt_for_number()
    if value is None:
        print("Please enter a valid integer.")
        return

    message = "is" if is_prime(value) else "is not"
    print(f"{value} {message} a prime number.")


if __name__ == "__main__":
    main()
