"""Question 26: calculate RMSE."""
from _common import linear, metrics
m,_,xt,_,yt=linear(); print(metrics(m,xt,yt)['RMSE'])
