"""Question 13: display the last five records."""

from _common import load_iris_dataframe


def main() -> None:
    print(load_iris_dataframe().tail())


if __name__ == "__main__":
    main()