"""Question 14: compare clustering before and after scaling."""
from sklearn.cluster import KMeans
from _common import features, scaled
print({'unscaled':KMeans(3,n_init=10,random_state=42).fit(features()).inertia_,'scaled':KMeans(3,n_init=10,random_state=42).fit(scaled()).inertia_})
