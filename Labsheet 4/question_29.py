"""Question 29: interpret MSE and R2."""
from _common import linear, metrics
m,_,xt,_,yt=linear(); values=metrics(m,xt,yt); print('Lower MSE is better; R2 closer to 1 is better.'); print(values)
