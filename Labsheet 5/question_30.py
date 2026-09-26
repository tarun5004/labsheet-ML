"""Question 30: calculate a silhouette score."""
from sklearn.metrics import silhouette_score
from _common import kmeans, scaled
values=scaled(); model=kmeans(); print(silhouette_score(values,model.labels_))
