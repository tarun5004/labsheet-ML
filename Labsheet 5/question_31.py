"""Question 31: compare silhouette scores for K values."""
from sklearn.metrics import silhouette_score
from _common import kmeans, scaled
values=scaled()
for k in range(2,7): print(k, silhouette_score(values,kmeans(k).labels_))
