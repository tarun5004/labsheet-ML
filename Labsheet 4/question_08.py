"""Question 8: predict output values."""
from _common import linear
model,_,x_test,_,_=linear(); print(model.predict(x_test.head()))
