"""Question 16: compare actual and predicted values graphically."""
import matplotlib.pyplot as plt
from _common import linear, save_plot
model,_,x_test,_,y_test=linear(); plt.scatter(y_test,model.predict(x_test)); plt.xlabel('Actual'); plt.ylabel('Predicted'); save_plot('question_16_actual_predicted.png')
