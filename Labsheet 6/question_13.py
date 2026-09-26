"""Question 13: compare discount factors."""
from _common import train
for gamma in (.5,.8,.95): print(gamma,train(gamma=gamma)[2][-20:].mean())
