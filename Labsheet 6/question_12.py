"""Question 12: compare learning rates."""
from _common import train
for alpha in (.05,.1,.3): print(alpha,train(alpha=alpha)[2][-20:].mean())
