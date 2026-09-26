"""Question 18: display complete dataset information."""

from _common import load_iris_dataframe


def main() -> None:
    load_iris_dataframe().info()


if __name__ == "__main__":
    main()