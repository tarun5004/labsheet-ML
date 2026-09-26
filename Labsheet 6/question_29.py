"""Question 29: save the learned DQN-style table."""
import numpy as np
from _common import train, OUTPUT_DIR
_,table,_=train(); OUTPUT_DIR.mkdir(exist_ok=True); np.save(OUTPUT_DIR/'dqn_style_model.npy',table); print('model saved')
