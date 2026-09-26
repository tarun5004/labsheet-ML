"""Question 10: determine K with the elbow method."""
import matplotlib.pyplot as plt
from _common import kmeans, save_plot
values=[kmeans(k).inertia_ for k in range(1,9)]; plt.plot(range(1,9),values,marker='o'); plt.xlabel('K'); plt.ylabel('Inertia'); save_plot('question_10_elbow.png')
