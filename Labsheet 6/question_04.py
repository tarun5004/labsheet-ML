"""Question 4: display state, action, reward, and termination."""
from _common import GridWorld
env=GridWorld(); state=env.reset(); next_state,reward,done=env.step(3); print(state,3,reward,done,next_state)
