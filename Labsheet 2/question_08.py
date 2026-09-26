"""Question 8: fill missing values using forward fill."""
from _common import messy
print(messy().ffill().isna().sum())
