"""Question 15: implement agglomerative clustering."""
from sklearn.cluster import AgglomerativeClustering
from _common import scaled
print(AgglomerativeClustering(n_clusters=3).fit_predict(scaled()))
