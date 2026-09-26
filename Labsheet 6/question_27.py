"""Question 27: analyze replay-memory effect."""
from _common import train
for episodes in (50,300,800): print(episodes,train(episodes)[2][-20:].mean())
