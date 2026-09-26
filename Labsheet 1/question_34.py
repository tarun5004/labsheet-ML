"""Question 34: create a scatter plot for two variables."""

import matplotlib.pyplot as plt

from _common import OUTPUT_DIR, load_iris_dataframe


def main() -> None:
    dataset = load_iris_dataframe()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for species, group in dataset.groupby("species"):
        plt.scatter(group["sepal_length_cm"], group["petal_length_cm"], label=species)
    plt.title("Sepal length versus petal length")
    plt.xlabel("Sepal length (cm)")
    plt.ylabel("Petal length (cm)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "question_34_scatter_plot.png", dpi=150)
    plt.close()
    print("Saved question_34_scatter_plot.png")


if __name__ == "__main__":
    main()