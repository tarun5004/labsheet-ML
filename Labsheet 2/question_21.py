"""Question 21: apply robust scaling."""
from sklearn.preprocessing import RobustScaler
from _common import scaled
print(scaled(RobustScaler()).head())
