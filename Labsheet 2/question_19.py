"""Question 19: apply Min-Max normalization."""
from sklearn.preprocessing import MinMaxScaler
from _common import scaled
print(scaled(MinMaxScaler()).head())
