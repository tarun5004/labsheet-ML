"""Question 10: compare before and after missing-value treatment."""
from _common import messy
before = messy(); after = before.copy(); after["sepal_length"] = after["sepal_length"].fillna(after["sepal_length"].mean()); after["species"] = after["species"].fillna(after["species"].mode()[0]); print({'before': int(before.isna().sum().sum()), 'after': int(after.isna().sum().sum())})
