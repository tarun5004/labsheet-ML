"""Question 16: check the data types of all columns."""

from _common import load_iris_dataframe


def main() -> None:
    print(load_iris_dataframe().dtypes)


if __name__ == "__main__":
    main()