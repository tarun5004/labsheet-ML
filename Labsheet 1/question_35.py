"""Question 35: create and visualize a correlation matrix."""

import matplotlib.pyplot as plt
import seaborn as sns

from _common import OUTPUT_DIR, load_iris_dataframe


def main() -> None:
    dataset = load_iris_dataframe().drop(columns="species")
    correlation = dataset.corr(numeric_only=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    correlation.to_csv(OUTPUT_DIR / "question_35_correlation_matrix.csv")
    sns.heatmap(correlation, annot=True, cmap="viridis", fmt=".2f")
    plt.title("Iris feature correlation matrix")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "question_35_heatmap.png", dpi=150)
    plt.close()
    print(correlation)
    print("Saved correlation matrix and heatmap")


if __name__ == "__main__":
    main()