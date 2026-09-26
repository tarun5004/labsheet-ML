"""Question 6: implement simple linear regression."""
from sklearn.linear_model import LinearRegression
from _common import split
x_train,x_test,y_train,y_test=split(); model=LinearRegression(); model.fit(x_train[['bmi']],y_train); print(model.coef_)
