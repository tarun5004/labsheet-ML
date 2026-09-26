"""Shared helpers for Labsheet 1 experiments."""

from pathlib import Path

import pandas as pd
from sklearn.datasets import load_iris


LAB_DIR = Path(__file__).parent
OUTPUT_DIR = LAB_DIR / "outputs"


def load_iris_dataframe() -> pd.DataFrame:
    """Return the bundled Iris dataset with readable column names."""
    iris = load_iris(as_frame=True)
    dataset = iris.frame.rename(
        columns={
            "sepal length (cm)": "sepal_length_cm",
            "sepal width (cm)": "sepal_width_cm",
            "petal length (cm)": "petal_length_cm",
            "petal width (cm)": "petal_width_cm",
            "target": "target_id",
        }
    )
    dataset["species"] = dataset["target_id"].map(dict(enumerate(iris.target_names)))
    return dataset


def save_output(data: pd.DataFrame, filename: str) -> Path:
    """Save a DataFrame in the labsheet output directory."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / filename
    data.to_csv(output_path, index=False)
    return output_path