"""Question 29: compare clustering before and after PCA."""
from _common import kmeans, pca_data
print({'original':kmeans().inertia_,'pca':kmeans(3,pca_data()).inertia_})
