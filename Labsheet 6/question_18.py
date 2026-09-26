"""Question 18: visualize the learned optimal path."""
import matplotlib.pyplot as plt
from _common import train, greedy_path, OUTPUT_DIR
_,table,_=train(); path=greedy_path(table); plt.plot([p%4 for p in path],[p//4 for p in path],marker='o'); plt.gca().invert_yaxis(); OUTPUT_DIR.mkdir(exist_ok=True); plt.savefig(OUTPUT_DIR/'question_18_path.png'); plt.close(); print(path)
