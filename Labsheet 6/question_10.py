"""Question 10: evaluate the trained agent."""
from _common import train, greedy_path
_,table,_=train(); print('path:',greedy_path(table))
