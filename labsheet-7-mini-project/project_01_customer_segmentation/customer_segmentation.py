"""Project 1: customer segmentation with K-Means and hierarchical clustering.

This beginner-friendly example creates a small purchasing dataset so that it
can run without downloading a private customer file.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.cluster import AgglomerativeClustering, KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler


PROJECT_DIR = Path(__file__).parent
OUTPUT_DIR = PROJECT_DIR / "outputs"


def make_customer_data(seed=42, customers_per_group=60):
    """Create realistic-looking customer data for classroom practice."""
    rng = np.random.default_rng(seed)
    groups = [
        (28, 32, 25, 2),
        (42, 85, 20, 9),
        (35, 45, 75, 5),
        (51, 72, 68, 7),
    ]
    rows = []
    for age, income, spending, purchases in groups:
        for _ in range(customers_per_group):
            rows.append(
                {
                    "age": max(18, rng.normal(age, 4)),
                    "annual_income": max(15, rng.normal(income, 7)),
                    "spending_score": np.clip(rng.normal(spending, 8), 1, 100),
                    "purchases_per_year": max(1, rng.normal(purchases, 1.2)),
                }
            )
    return pd.DataFrame(rows).round(2)


def choose_cluster_count(features, minimum=2, maximum=8):
    """Select k using the highest silhouette score."""
    scores = {}
    for cluster_count in range(minimum, maximum + 1):
        labels = KMeans(n_clusters=cluster_count, random_state=42, n_init=10).fit_predict(features)
        scores[cluster_count] = silhouette_score(features, labels)
    best_count = max(scores, key=scores.get)
    return best_count, scores


def save_cluster_plot(data, labels, title, filename):
    """Save a readable two-dimensional PCA view of the clusters."""
    projection = PCA(n_components=2, random_state=42).fit_transform(data)
    plot_data = pd.DataFrame({"component_1": projection[:, 0], "component_2": projection[:, 1], "cluster": labels})
    sns.scatterplot(data=plot_data, x="component_1", y="component_2", hue="cluster", palette="deep", s=65)
    plt.title(title)
    plt.xlabel("PCA component 1")
    plt.ylabel("PCA component 2")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / filename, dpi=150)
    plt.close()


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    customers = make_customer_data()
    feature_names = ["age", "annual_income", "spending_score", "purchases_per_year"]
    scaled_features = StandardScaler().fit_transform(customers[feature_names])

    cluster_count, scores = choose_cluster_count(scaled_features)
    kmeans = KMeans(n_clusters=cluster_count, random_state=42, n_init=10)
    customers["kmeans_cluster"] = kmeans.fit_predict(scaled_features)
    hierarchical = AgglomerativeClustering(n_clusters=cluster_count)
    customers["hierarchical_cluster"] = hierarchical.fit_predict(scaled_features)

    kmeans_silhouette = silhouette_score(scaled_features, customers["kmeans_cluster"])
    hierarchical_silhouette = silhouette_score(scaled_features, customers["hierarchical_cluster"])
    customers.to_csv(OUTPUT_DIR / "customer_segments.csv", index=False)
    save_cluster_plot(scaled_features, customers["kmeans_cluster"], "Customer segments - K-Means", "customer_kmeans_clusters.png")
    save_cluster_plot(scaled_features, customers["hierarchical_cluster"], "Customer segments - hierarchical", "customer_hierarchical_clusters.png")

    print("Customer Segmentation")
    print("---------------------")
    print(f"Best number of clusters: {cluster_count}")
    print("Silhouette scores by k:", {k: round(value, 3) for k, value in scores.items()})
    print(f"K-Means silhouette score: {kmeans_silhouette:.3f}")
    print(f"Hierarchical silhouette score: {hierarchical_silhouette:.3f}")
    print("\nK-Means cluster profile:")
    print(customers.groupby("kmeans_cluster")[feature_names].mean().round(1).to_string())
    print(f"\nFiles saved in: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()