"""Question 25: calculate MSE."""
from _common import linear, metrics
m,_,xt,_,yt=linear(); print(metrics(m,xt,yt)['MSE'])
