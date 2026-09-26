"""Question 24: plot episode rewards for the DQN-style agent."""
from _common import train, plot_rewards
_,_,rewards=train(500); print(plot_rewards(rewards,'question_24_dqn_rewards.png'))
