"""Question 15: predict with the testing dataset."""
from _common import linear
model,_,x_test,_,_=linear(); print(model.predict(x_test).shape)
