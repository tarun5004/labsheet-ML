"""Question 1: verify the installed Python version."""

import sys


def main() -> None:
    print(f"Python version: {sys.version.split()[0]}")


if __name__ == "__main__":
    main()