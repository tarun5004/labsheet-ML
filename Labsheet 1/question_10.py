"""Question 10: display virtual-environment setup commands."""


def main() -> None:
    print("Create:  python -m venv .venv")
    print("Windows: .venv\\Scripts\\Activate.ps1")
    print("Install: python -m pip install -r requirements.txt")


if __name__ == "__main__":
    main()