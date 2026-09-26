"""Question 22: apply PCA."""
from sklearn.decomposition import PCA
from _common import scaled
print(PCA().fit_transform(scaled()).shape)
