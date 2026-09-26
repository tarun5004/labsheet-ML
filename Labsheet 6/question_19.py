"""Question 19: compare environment performance."""
from _common import train
_,_,r=train(); print({'grid_world_mean_reward':r.mean(),'episodes':len(r)})
