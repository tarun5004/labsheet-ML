"""Question 14: visualize outliers with a scatter plot."""
import matplotlib.pyplot as plt
from _common import OUTPUT_DIR, dataset
OUTPUT_DIR.mkdir(exist_ok=True); frame=dataset(); plt.scatter(frame.sepal_length, frame.petal_length); plt.tight_layout(); plt.savefig(OUTPUT_DIR / 'question_14_scatter.png'); plt.close()
