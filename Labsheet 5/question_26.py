"""Question 26: calculate cumulative explained variance."""
from sklearn.decomposition import PCA
from _common import scaled
print(PCA().fit(scaled()).explained_variance_ratio_.cumsum())
