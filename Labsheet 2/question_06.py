"""Question 6: fill numerical missing values with the median."""
from _common import messy
frame = messy(); frame["sepal_length"] = frame["sepal_length"].fillna(frame["sepal_length"].median()); print(frame.isna().sum())
