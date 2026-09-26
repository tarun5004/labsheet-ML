"""Question 28: add a new column."""

from _common import load_iris_dataframe


def main() -> None:
    dataset = load_iris_dataframe()
    dataset["sepal_area_cm2"] = dataset["sepal_length_cm"] * dataset["sepal_width_cm"]
    print(dataset.head())


if __name__ == "__main__":
    main()