"""Question 14: compare exploration rates."""
from _common import train
for epsilon in (.05,.2,.5): print(epsilon,train(epsilon=epsilon)[2].mean())
