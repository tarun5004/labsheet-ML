"""Question 4: remove columns with more than 50% missing values."""
from _common import messy
frame = messy(); print(frame.dropna(axis=1, thresh=len(frame) * .5).columns.tolist())
