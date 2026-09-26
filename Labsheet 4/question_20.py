"""Question 20: compare linear and polynomial regression."""
from _common import linear, polynomial, metrics
lm,_,xt,_,yt=linear(); pm,*_=polynomial(2); print('linear',metrics(lm,xt,yt)); print('polynomial',metrics(pm,xt,yt))
