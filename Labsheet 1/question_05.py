"""Question 5: create a simple line plot with Matplotlib."""

import matplotlib.pyplot as plt

from _common import OUTPUT_DIR


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], marker="o")
    plt.title("Simple line plot")
    plt.xlabel("X")
    plt.ylabel("X squared")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "question_05_line_plot.png", dpi=150)
    plt.close()
    print("Saved question_05_line_plot.png")


if __name__ == "__main__":
    main()