"""Question 31: save the modified dataset as a new CSV."""

from _common import load_iris_dataframe, save_output


def main() -> None:
    dataset = load_iris_dataframe().drop(columns="target_id")
    print(f"Saved: {save_output(dataset, 'iris_modified.csv')}")


if __name__ == "__main__":
    main()