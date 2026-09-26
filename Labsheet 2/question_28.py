"""Question 28: one-hot encode a categorical variable."""
from _common import dataset
print(__import__('pandas').get_dummies(dataset(), columns=['species']).head())
