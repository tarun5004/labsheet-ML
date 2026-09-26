"""Question 27: calculate R-squared."""
from _common import linear, metrics
m,_,xt,_,yt=linear(); print(metrics(m,xt,yt)['R2'])
