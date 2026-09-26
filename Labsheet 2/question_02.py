"""Question 2: display missing-value percentages."""
from _common import messy
print(messy().isna().mean().mul(100).round(2))
