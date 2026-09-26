"""Question 23: train a DQN-style agent on a CartPole-like task."""
from _common import train
_,table,rewards=train(500); print({'episodes':len(rewards),'best':rewards.max(),'parameters':table.size})
