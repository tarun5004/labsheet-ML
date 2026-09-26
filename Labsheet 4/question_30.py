"""Question 30: visualize prediction errors."""
import matplotlib.pyplot as plt
from _common import linear, save_plot
m,_,xt,_,yt=linear(); errors=yt-m.predict(xt); plt.scatter(m.predict(xt),errors); plt.axhline(0,color='red'); plt.xlabel('Prediction'); plt.ylabel('Error'); save_plot('question_30_errors.png')
