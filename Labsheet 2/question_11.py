"""Question 11: detect outliers with IQR."""
from _common import messy
frame = messy(); print((~__import__('_common').outlier_mask(frame)).sum())
