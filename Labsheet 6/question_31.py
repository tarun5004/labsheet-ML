"""Question 31: compare cumulative rewards."""
from _common import train
for name,epsilon in [('q_learning',.2),('dqn_style',.05)]: print(name,train(500,epsilon=epsilon)[2].sum())
