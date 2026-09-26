"""Question 28: K-Means on PCA data."""
from _common import kmeans, pca_data
print(kmeans(3,pca_data()).labels_)
