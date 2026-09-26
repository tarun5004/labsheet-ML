"""Question 22: count the frequency of each unique value."""

from _common import load_iris_dataframe


def main() -> None:
    print(load_iris_dataframe()["species"].value_counts())


if __name__ == "__main__":
    main()