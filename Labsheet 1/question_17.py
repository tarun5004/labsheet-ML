"""Question 17: generate descriptive statistics."""

from _common import load_iris_dataframe


def main() -> None:
    print(load_iris_dataframe().describe())


if __name__ == "__main__":
    main()