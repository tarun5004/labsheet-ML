"""Question 25: evaluate the DQN-style agent."""
from _common import train, greedy_path
_,table,_=train(500); print(greedy_path(table))
