"""Question 9: visualize the regression line."""
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from _common import split, save_plot
x_train,x_test,y_train,y_test=split(); model=LinearRegression().fit(x_train[['bmi']],y_train); plt.scatter(x_test.bmi,y_test); plt.plot(x_test.bmi,model.predict(x_test[['bmi']]),color='red'); save_plot('question_09_regression_line.png')
