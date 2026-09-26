"""Question 22: define a lightweight DQN-style value approximator."""
import numpy as np
from _common import GridWorld
env=GridWorld(); weights=np.zeros((env.n_states,env.n_actions)); print(weights.shape)
