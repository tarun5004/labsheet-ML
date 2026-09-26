"""Question 24: calculate MAE."""
from _common import linear, metrics
m,_,xt,_,yt=linear(); print(metrics(m,xt,yt)['MAE'])
