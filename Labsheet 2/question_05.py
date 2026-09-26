"""Question 5: fill numerical missing values with the mean."""
from _common import messy
frame = messy(); frame["sepal_length"] = frame["sepal_length"].fillna(frame["sepal_length"].mean()); print(frame.isna().sum())
