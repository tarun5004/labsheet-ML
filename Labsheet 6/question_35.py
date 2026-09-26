"""Question 35: print a comparative RL report summary."""
from _common import train
q=train(500,epsilon=.2)[2]; d=train(500,epsilon=.05)[2]; print({'Q-Learning mean':q.mean(),'DQN-style mean':d.mean(),'Q-Learning final':q[-50:].mean(),'DQN-style final':d[-50:].mean()})
