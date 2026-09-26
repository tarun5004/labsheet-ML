"""Question 7: fill categorical missing values with the mode."""
from _common import messy
frame = messy(); frame["species"] = frame["species"].fillna(frame["species"].mode()[0]); print(frame["species"].isna().sum())
