"""Question 26: compare Q-Learning and DQN-style results."""
from _common import train
_,_,q=train(300,epsilon=.2); _,_,d=train(300,epsilon=.05); print({'q_learning':q[-50:].mean(),'dqn_style':d[-50:].mean()})
