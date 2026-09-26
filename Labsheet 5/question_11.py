"""Question 11: visualize clusters."""
import matplotlib.pyplot as plt
from _common import kmeans, scaled, save_plot
labels=kmeans().labels_; plt.scatter(scaled()[:,0],scaled()[:,1],c=labels); save_plot('question_11_clusters.png')
