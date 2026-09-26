"""Question 19: identify missing values."""

from _common import load_iris_dataframe


def main() -> None:
    print(load_iris_dataframe().isna())


if __name__ == "__main__":
    main()