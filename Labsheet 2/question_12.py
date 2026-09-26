"""Question 12: detect outliers with Z-scores."""
from scipy.stats import zscore
from _common import numeric
scores = numeric().apply(zscore).abs(); print((scores > 3).any(axis=1).sum())
