"""Question 9: compare different K values."""
from _common import kmeans
for k in range(2,6): print(k,kmeans(k).inertia_)
