"""Question 34: select features using correlation analysis."""
from _common import numeric
correlation=numeric().corr().abs(); print(correlation['petal_length'].sort_values(ascending=False))
