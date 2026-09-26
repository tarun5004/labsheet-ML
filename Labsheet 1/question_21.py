"""Question 21: display unique values in a selected column."""

from _common import load_iris_dataframe


def main() -> None:
    print(load_iris_dataframe()["species"].unique())


if __name__ == "__main__":
    main()