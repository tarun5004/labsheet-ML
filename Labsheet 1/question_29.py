"""Question 29: delete an existing column."""

from _common import load_iris_dataframe


def main() -> None:
    dataset = load_iris_dataframe().drop(columns="target_id")
    print(dataset.columns.tolist())


if __name__ == "__main__":
    main()