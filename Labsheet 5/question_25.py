"""Question 25: display explained variance ratio."""
from sklearn.decomposition import PCA
from _common import scaled
print(PCA().fit(scaled()).explained_variance_ratio_)
