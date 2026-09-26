"""Question 24: visualize PCA transformed data."""
import matplotlib.pyplot as plt
from _common import pca_data, save_plot
values=pca_data(); plt.scatter(values[:,0],values[:,1]); plt.xlabel('PC1'); plt.ylabel('PC2'); save_plot('question_24_pca_scatter.png')
