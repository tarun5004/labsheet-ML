"""Question 25: visualize scaling with box plots."""
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from _common import OUTPUT_DIR, scaled
OUTPUT_DIR.mkdir(exist_ok=True); scaled(StandardScaler()).plot.box(); plt.tight_layout(); plt.savefig(OUTPUT_DIR / 'question_25_boxplots.png'); plt.close()
