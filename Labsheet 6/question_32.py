"""Question 32: visualize the learning curve."""
from _common import train, plot_rewards
print(plot_rewards(train(500)[2],'question_32_learning_curve.png'))
