"""Question 3: explore information and summary statistics."""
from _common import data
frame=data(); frame.info(); print(frame.describe()); print(frame.dtypes)
