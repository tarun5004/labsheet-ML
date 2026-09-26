"""Question 11: plot cumulative rewards."""
from _common import train, plot_rewards
_,_,rewards=train(); print(plot_rewards(rewards,'question_11_rewards.png'))
