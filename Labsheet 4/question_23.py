"""Question 23: compare polynomial degrees."""
from _common import polynomial, metrics
for degree in (1,2,3):
 model,_,xt,_,yt=polynomial(degree); print(degree, metrics(model,xt,yt))
