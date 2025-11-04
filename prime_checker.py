"""Utility to check if a number is prime.

Run this module directly to input a number and check primality.
"""

import math


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


def main() -> None:
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
