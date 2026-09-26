"""Question 21: compare hierarchical and K-Means clustering."""
from sklearn.cluster import AgglomerativeClustering
from _common import kmeans, scaled
print({'kmeans':kmeans().inertia_,'hierarchical':AgglomerativeClustering(3).fit(scaled()).labels_.size})
