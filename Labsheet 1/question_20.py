"""Question 20: count missing values in each column."""

from _common import load_iris_dataframe


def main() -> None:
    print(load_iris_dataframe().isna().sum())


if __name__ == "__main__":
    main()