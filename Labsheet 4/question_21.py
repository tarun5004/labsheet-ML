"""Question 21: visualize polynomial curves."""
import matplotlib.pyplot as plt
from _common import polynomial, save_plot
model,_,x_test,_,y_test=polynomial(2); plt.scatter(y_test,model.predict(x_test)); plt.xlabel('Actual'); plt.ylabel('Polynomial prediction'); save_plot('question_21_polynomial_curve.png')
