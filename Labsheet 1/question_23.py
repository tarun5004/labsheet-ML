"""Question 23: rename a dataset column."""

from _common import load_iris_dataframe


def main() -> None:
    dataset = load_iris_dataframe().rename(columns={"species": "class_name"})
    print(dataset.columns.tolist())


if __name__ == "__main__":
    main()