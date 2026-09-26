"""Shared regression helpers for Labsheet 4."""
from pathlib import Path
import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

LAB_DIR = Path(__file__).parent
OUTPUT_DIR = LAB_DIR / "outputs"

def data():
    source = load_diabetes(as_frame=True)
    return source.data, source.target

def split():
    features, target = data()
    return train_test_split(features, target, test_size=.2, random_state=42)

def linear():
    x_train, x_test, y_train, y_test = split()
    model = LinearRegression().fit(x_train, y_train)
    return model, x_train, x_test, y_train, y_test

def polynomial(degree=2):
    x_train, x_test, y_train, y_test = split()
    model = make_pipeline(PolynomialFeatures(degree), LinearRegression()).fit(x_train, y_train)
    return model, x_train, x_test, y_train, y_test

def metrics(model, x_test, y_test):
    prediction = model.predict(x_test)
    mse = mean_squared_error(y_test, prediction)
    return {'MAE': mean_absolute_error(y_test, prediction), 'MSE': mse, 'RMSE': np.sqrt(mse), 'R2': r2_score(y_test, prediction)}

def save_plot(name):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUTPUT_DIR / name
    plt.tight_layout(); plt.savefig(path, dpi=140); plt.close()
    return path
