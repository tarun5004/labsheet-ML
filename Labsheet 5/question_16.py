"""Question 16: generate a dendrogram."""
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from _common import scaled, save_plot
Z=linkage(scaled(),method='ward'); dendrogram(Z,no_labels=True); save_plot('question_16_dendrogram.png')
