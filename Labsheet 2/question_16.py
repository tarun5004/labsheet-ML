"""Question 16: replace outliers with median values."""
from _common import messy, numeric
frame=messy(); values=numeric(frame); med=values.median(); condition=(values-med).abs()>3*values.std(); frame[values.columns]=values.mask(condition, med, axis="columns"); print(frame.head())
