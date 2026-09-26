"""Shared clustering and PCA helpers for Labsheet 5."""
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

LAB_DIR = Path(__file__).parent
OUTPUT_DIR = LAB_DIR / "outputs"

def data():
    iris = load_iris(as_frame=True)
    frame = iris.frame.rename(columns={
        'sepal length (cm)': 'sepal_length', 'sepal width (cm)': 'sepal_width',
        'petal length (cm)': 'petal_length', 'petal width (cm)': 'petal_width', 'target': 'species_id'})
    return frame

def features():
    return data().drop(columns='species_id')

def scaled():
    return StandardScaler().fit_transform(features())

def kmeans(k=3, values=None):
    return KMeans(n_clusters=k, random_state=42, n_init=10).fit(values if values is not None else scaled())

def pca_data():
    return PCA(n_components=2, random_state=42).fit_transform(scaled())

def save_plot(name):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUTPUT_DIR / name
    plt.tight_layout(); plt.savefig(path, dpi=140); plt.close()
    return path
