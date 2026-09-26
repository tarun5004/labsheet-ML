"""Question 11: load a CSV dataset with Pandas."""

from _common import load_iris_dataframe, save_output
import pandas as pd


def main() -> None:
    source_path = save_output(load_iris_dataframe(), "iris_source.csv")
    dataset = pd.read_csv(source_path)
    print(dataset.head())


if __name__ == "__main__":
    main()