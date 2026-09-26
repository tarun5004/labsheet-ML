"""Question 33: visualize cluster distributions."""
import seaborn as sns
from _common import data, kmeans, save_plot
frame=data(); frame['cluster']=kmeans().labels_; sns.pairplot(frame,hue='cluster'); save_plot('question_33_pairplot.png')
