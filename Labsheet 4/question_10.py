"""Question 10: compare actual and predicted values."""
from _common import linear
model,_,x_test,_,y_test=linear(); print(list(zip(y_test.head().round(1), model.predict(x_test.head()).round(1))))
