"""Question 17: use Ward linkage."""
from sklearn.cluster import AgglomerativeClustering
from _common import scaled
print(AgglomerativeClustering(n_clusters=3,linkage='ward').fit_predict(scaled()))
