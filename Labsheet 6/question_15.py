"""Question 15: demonstrate epsilon-greedy selection."""
import numpy as np
from _common import choose_action
q=np.array([[1.,4.,2.,0.]]); rng=np.random.default_rng(4); print([choose_action(q,0,.2,rng) for _ in range(10)])
