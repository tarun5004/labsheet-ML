"""Question 28: compare linear and polynomial metrics."""
from _common import linear, polynomial, metrics
lm,_,xt,_,yt=linear(); pm,*_=polynomial(2); print({'linear':metrics(lm,xt,yt),'polynomial':metrics(pm,xt,yt)})
