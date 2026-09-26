"""Question 13: assign labels to the original dataset."""
from _common import data, kmeans
frame=data(); frame['cluster']=kmeans().labels_; print(frame.head())
