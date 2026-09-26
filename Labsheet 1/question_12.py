"""Question 12: display the first five records."""

from _common import load_iris_dataframe


def main() -> None:
    print(load_iris_dataframe().head())


if __name__ == "__main__":
    main()