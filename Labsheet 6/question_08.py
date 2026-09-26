"""Question 8: train over multiple episodes."""
from _common import train
_,_,rewards=train(500); print(len(rewards),rewards[-10:])
