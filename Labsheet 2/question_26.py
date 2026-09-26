"""Question 26: compare scaling techniques."""
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, MaxAbsScaler
from _common import scaled
for name, scaler in [('minmax',MinMaxScaler()),('standard',StandardScaler()),('robust',RobustScaler()),('maxabs',MaxAbsScaler())]: print(name, scaled(scaler).std().round(2).to_dict())
