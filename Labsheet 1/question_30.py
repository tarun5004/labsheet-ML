"""Question 30: remove duplicate records."""

import pandas as pd

from _common import load_iris_dataframe


def main() -> None:
    dataset = load_iris_dataframe()
    with_duplicate = pd.concat([dataset, dataset.iloc[[0]]], ignore_index=True)
    without_duplicates = with_duplicate.drop_duplicates()
    print(f"Before: {len(with_duplicate)}\nAfter: {len(without_duplicates)}")


if __name__ == "__main__":
    main()