"""Question 9: fill missing values using backward fill."""
from _common import messy
print(messy().bfill().isna().sum())
