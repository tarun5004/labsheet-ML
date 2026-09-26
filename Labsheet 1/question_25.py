"""Question 25: select rows and columns using iloc[]."""

from _common import load_iris_dataframe


def main() -> None:
    print(load_iris_dataframe().iloc[0:5, 0:3])


if __name__ == "__main__":
    main()