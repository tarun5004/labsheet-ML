"""Question 33: create a histogram with Matplotlib."""

import matplotlib.pyplot as plt

from _common import OUTPUT_DIR, load_iris_dataframe


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    plt.hist(load_iris_dataframe()["sepal_length_cm"], bins=10, edgecolor="black")
    plt.title("Sepal length distribution")
    plt.xlabel("Sepal length (cm)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "question_33_histogram.png", dpi=150)
    plt.close()
    print("Saved question_33_histogram.png")


if __name__ == "__main__":
    main()