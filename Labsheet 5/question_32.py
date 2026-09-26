"""Question 32: analyze cluster characteristics."""
from _common import data, kmeans
frame=data(); frame['cluster']=kmeans().labels_; print(frame.groupby('cluster').mean(numeric_only=True))
