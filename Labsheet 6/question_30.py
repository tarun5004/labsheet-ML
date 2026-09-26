"""Question 30: load and test the saved model."""
import numpy as np
from _common import train, OUTPUT_DIR, greedy_path
path=OUTPUT_DIR/'dqn_style_model.npy'
if not path.exists(): OUTPUT_DIR.mkdir(exist_ok=True); np.save(path,train()[1])
print(greedy_path(np.load(path)))
