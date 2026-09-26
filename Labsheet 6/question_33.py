"""Question 33: compare training time and convergence."""
import time
from _common import train
for name in ('q_learning','dqn_style'):
 start=time.perf_counter(); rewards=train(500,epsilon=.2 if name=='q_learning' else .05)[2]; print(name,time.perf_counter()-start,rewards[-50:].mean())
