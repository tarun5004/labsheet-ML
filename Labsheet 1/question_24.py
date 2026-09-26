"""Question 24: select rows and columns using loc[]."""

from _common import load_iris_dataframe


def main() -> None:
    print(load_iris_dataframe().loc[0:4, ["sepal_length_cm", "species"]])


if __name__ == "__main__":
    main()