"""Question 26: filter records using a condition."""

from _common import load_iris_dataframe


def main() -> None:
    filtered = load_iris_dataframe()[load_iris_dataframe()["petal_length_cm"] > 5.0]
    print(filtered)


if __name__ == "__main__":
    main()