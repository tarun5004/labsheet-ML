"""Question 20: visualize hierarchical clusters."""
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from _common import scaled, save_plot
labels=AgglomerativeClustering(3).fit_predict(scaled()); plt.scatter(scaled()[:,0],scaled()[:,1],c=labels); save_plot('question_20_hierarchical.png')
