"""Question 17: analyze feature effects."""
from _common import linear
model,*_=linear(); print(dict(zip(model.feature_names_in_,model.coef_.round(2))))
