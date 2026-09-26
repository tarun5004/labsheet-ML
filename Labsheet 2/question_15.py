"""Question 15: remove outliers with IQR."""
from _common import messy, outlier_mask
frame = messy(); print(frame[outlier_mask(frame)].shape)
