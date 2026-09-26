"""Shared data and preprocessing helpers for Labsheet 2."""
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, MaxAbsScaler, LabelEncoder

LAB_DIR = Path(__file__).parent
OUTPUT_DIR = LAB_DIR / "outputs"

def dataset():
    iris = load_iris(as_frame=True)
    frame = iris.frame.rename(columns={
        "sepal length (cm)": "sepal_length", "sepal width (cm)": "sepal_width",
        "petal length (cm)": "petal_length", "petal width (cm)": "petal_width",
        "target": "target_id",
    })
    frame["species"] = frame["target_id"].map(dict(enumerate(iris.target_names)))
    frame["date"] = pd.date_range("2024-01-01", periods=len(frame), freq="D")
    return frame

def messy():
    frame = dataset().copy()
    frame.loc[[2, 7], "sepal_length"] = np.nan
    frame.loc[10, "species"] = np.nan
    frame.loc[0, "petal_length"] = 20
    frame["mostly_missing"] = np.nan
    return frame

def numeric(frame=None):
    frame = (frame if frame is not None else dataset()).select_dtypes("number")
    return frame.drop(columns=["target_id"], errors="ignore")

def save(frame, name):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUTPUT_DIR / name
    frame.to_csv(path, index=False)
    return path

def scaled(scaler):
    frame = dataset()
    values = scaler.fit_transform(numeric(frame))
    return pd.DataFrame(values, columns=numeric(frame).columns)

def outlier_mask(frame):
    values = numeric(frame)
    lower = values.quantile(.25) - 1.5 * (values.quantile(.75) - values.quantile(.25))
    upper = values.quantile(.75) + 1.5 * (values.quantile(.75) - values.quantile(.25))
    return ~((values < lower) | (values > upper)).any(axis=1)
