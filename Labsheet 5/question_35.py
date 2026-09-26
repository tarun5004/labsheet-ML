"""Question 35: summarize K-Means and hierarchical performance."""
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
from _common import kmeans, scaled
values=scaled(); km=kmeans(); hc=AgglomerativeClustering(3).fit_predict(values); print({'kmeans_silhouette':silhouette_score(values,km.labels_),'hierarchical_silhouette':silhouette_score(values,hc)})
