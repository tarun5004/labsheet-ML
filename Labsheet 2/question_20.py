"""Question 20: apply standardization."""
from sklearn.preprocessing import StandardScaler
from _common import scaled
print(scaled(StandardScaler()).head())
