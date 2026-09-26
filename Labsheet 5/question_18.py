"""Question 18: use complete linkage."""
from sklearn.cluster import AgglomerativeClustering
from _common import scaled
print(AgglomerativeClustering(n_clusters=3,linkage='complete').fit_predict(scaled()))
