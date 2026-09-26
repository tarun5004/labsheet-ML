"""Question 24: visualize normalization with histograms."""
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from _common import OUTPUT_DIR, scaled
OUTPUT_DIR.mkdir(exist_ok=True); scaled(MinMaxScaler()).hist(); plt.tight_layout(); plt.savefig(OUTPUT_DIR / 'question_24_histograms.png'); plt.close()
