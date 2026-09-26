"""Question 20: analyze Q-Learning convergence."""
from _common import train
import numpy as np
rewards=train()[2]; print({'first_50':rewards[:50].mean(),'last_50':rewards[-50:].mean(),'change':np.mean(rewards[-50:])-np.mean(rewards[:50])})
