"""Question 15: display all dataset columns."""

from _common import load_iris_dataframe


def main() -> None:
    print(list(load_iris_dataframe().columns))


if __name__ == "__main__":
    main()