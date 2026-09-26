"""Question 7: initialize and update a Q-table."""
import numpy as np
from _common import GridWorld
env=GridWorld(); table=np.zeros((env.n_states,env.n_actions)); state=env.reset(); next_state,reward,_=env.step(3); table[state,3]=reward; print(table[0])
