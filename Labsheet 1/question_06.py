"""Question 6: generate a basic statistical plot with Seaborn."""

import matplotlib.pyplot as plt
import seaborn as sns

from _common import OUTPUT_DIR, load_iris_dataframe


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    sns.set_theme(style="whitegrid")
    sns.boxplot(data=load_iris_dataframe(), x="species", y="sepal_length_cm")
    plt.title("Sepal length by species")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "question_06_seaborn_plot.png", dpi=150)
    plt.close()
    print("Saved question_06_seaborn_plot.png")


if __name__ == "__main__":
    main()