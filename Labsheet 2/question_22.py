"""Question 22: apply max-absolute scaling."""
from sklearn.preprocessing import MaxAbsScaler
from _common import scaled
print(scaled(MaxAbsScaler()).head())
