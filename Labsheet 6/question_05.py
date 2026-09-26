"""Question 5: simulate random actions in a FrozenLake-style environment."""
import numpy as np
from _common import GridWorld
env=GridWorld(); rng=np.random.default_rng(1); state=env.reset()
for _ in range(10): state,reward,done=env.step(int(rng.integers(4))); print(state,reward,done); 
