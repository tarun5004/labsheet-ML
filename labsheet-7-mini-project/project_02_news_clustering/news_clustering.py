"""Project 2: group similar news articles with TF-IDF and clustering.

The small built-in dataset keeps the project runnable during a viva without
requiring an internet connection or a news API key.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.cluster import AgglomerativeClustering, KMeans
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import silhouette_score


PROJECT_DIR = Path(__file__).parent
OUTPUT_DIR = PROJECT_DIR / "outputs"


def make_news_data():
    """Return simple sample articles from four easy-to-understand topics."""
    articles = {
        "technology": [
            "Artificial intelligence software helps companies automate customer support",
            "New smartphone processor improves battery life and camera performance",
            "Cloud computing platform launches tools for safer data storage",
            "Cybersecurity researchers discover a vulnerability in popular web browsers",
            "Robots and machine learning change the future of software development",
        ],
        "sports": [
            "Football team wins championship after a dramatic final match",
            "Tennis player reaches the tournament final with a strong serve",
            "Cricket captain announces the squad for the international series",
            "Olympic athletes prepare for competition with daily training sessions",
            "Basketball coach praises the defense after an important league victory",
        ],
        "business": [
            "Stock markets rise as investors respond to strong company earnings",
            "Bank announces new interest rates for small business loans",
            "Retail company opens stores and creates jobs in growing cities",
            "Economic report forecasts steady growth and lower inflation next year",
            "Technology company reports increased revenue from international sales",
        ],
        "health": [
            "Doctors study a new treatment that may improve heart health",
            "Research shows regular exercise supports better sleep and mental health",
            "Hospitals introduce a program for faster patient recovery",
            "Scientists develop a vaccine after a successful clinical trial",
            "Healthy diet and preventive care can reduce the risk of disease",
        ],
    }
    rows = [{"topic": topic, "article": article} for topic, texts in articles.items() for article in texts]
    return pd.DataFrame(rows)


def choose_cluster_count(features, minimum=2, maximum=6):
    """Choose the number of groups with the best silhouette score."""
    scores = {}
    for cluster_count in range(minimum, maximum + 1):
        labels = KMeans(n_clusters=cluster_count, random_state=42, n_init=10).fit_predict(features)
        scores[cluster_count] = silhouette_score(features, labels)
    return max(scores, key=scores.get), scores


def save_cluster_plot(features, labels, title, filename):
    """Reduce TF-IDF vectors to two dimensions and save a scatter plot."""
    coordinates = TruncatedSVD(n_components=2, random_state=42).fit_transform(features)
    plot_data = pd.DataFrame({"component_1": coordinates[:, 0], "component_2": coordinates[:, 1], "cluster": labels})
    sns.scatterplot(data=plot_data, x="component_1", y="component_2", hue="cluster", palette="deep", s=80)
    plt.title(title)
    plt.xlabel("TF-IDF component 1")
    plt.ylabel("TF-IDF component 2")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / filename, dpi=150)
    plt.close()


def print_top_words(vectorizer, model, number_of_words=5):
    """Print words with the highest average importance in every cluster."""
    words = vectorizer.get_feature_names_out()
    print("\nImportant words in each K-Means cluster:")
    for cluster_number, center in enumerate(model.cluster_centers_):
        top_indexes = center.argsort()[-number_of_words:][::-1]
        print(f"Cluster {cluster_number}: {', '.join(words[index] for index in top_indexes)}")


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    news = make_news_data()
    vectorizer = TfidfVectorizer(stop_words="english", min_df=1)
    tfidf_features = vectorizer.fit_transform(news["article"])
    best_count, scores = choose_cluster_count(tfidf_features)

    kmeans = KMeans(n_clusters=best_count, random_state=42, n_init=10)
    news["kmeans_cluster"] = kmeans.fit_predict(tfidf_features)
    hierarchical = AgglomerativeClustering(n_clusters=best_count, metric="cosine", linkage="average")
    news["hierarchical_cluster"] = hierarchical.fit_predict(tfidf_features.toarray())

    kmeans_score = silhouette_score(tfidf_features, news["kmeans_cluster"])
    hierarchical_score = silhouette_score(tfidf_features, news["hierarchical_cluster"])
    news.to_csv(OUTPUT_DIR / "clustered_news_articles.csv", index=False)
    save_cluster_plot(tfidf_features, news["kmeans_cluster"], "News article clusters - K-Means", "news_kmeans_clusters.png")
    save_cluster_plot(tfidf_features, news["hierarchical_cluster"], "News article clusters - hierarchical", "news_hierarchical_clusters.png")

    print("News Article Clustering")
    print("-----------------------")
    print(f"Articles: {len(news)}")
    print(f"Best number of clusters: {best_count}")
    print("Silhouette scores by k:", {k: round(value, 3) for k, value in scores.items()})
    print(f"K-Means silhouette score: {kmeans_score:.3f}")
    print(f"Hierarchical silhouette score: {hierarchical_score:.3f}")
    print_top_words(vectorizer, kmeans)
    print(f"\nFiles saved in: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()