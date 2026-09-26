"""Question 13: visualize outliers with a box plot."""
import matplotlib.pyplot as plt
from _common import OUTPUT_DIR, numeric
OUTPUT_DIR.mkdir(exist_ok=True); numeric().plot.box(); plt.tight_layout(); plt.savefig(OUTPUT_DIR / 'question_13_boxplot.png'); plt.close()
