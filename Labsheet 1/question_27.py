"""Question 27: sort records by a column."""

from _common import load_iris_dataframe


def main() -> None:
    print(load_iris_dataframe().sort_values("sepal_length_cm", ascending=False).head())


if __name__ == "__main__":
    main()