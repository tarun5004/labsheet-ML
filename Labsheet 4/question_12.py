"""Question 12: predict user-defined input values."""
from _common import data, linear
x,y=data(); model,*_=linear(); print(model.predict(x.iloc[[0,1]]))
