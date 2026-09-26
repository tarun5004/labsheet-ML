"""Question 23: compare original and normalized data."""
from sklearn.preprocessing import MinMaxScaler
from _common import dataset, scaled
print(dataset().head(2)); print(scaled(MinMaxScaler()).head(2))
