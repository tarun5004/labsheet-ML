"""Question 14: find the number of rows and columns."""

from _common import load_iris_dataframe


def main() -> None:
    rows, columns = load_iris_dataframe().shape
    print(f"Rows: {rows}\nColumns: {columns}")


if __name__ == "__main__":
    main()