"""Question 19: compare linkage methods."""
from sklearn.cluster import AgglomerativeClustering
from _common import scaled
for method in ('ward','complete','average','single'): print(method,AgglomerativeClustering(3,linkage=method).fit_predict(scaled())[:10])
