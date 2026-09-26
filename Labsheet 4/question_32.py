"""Question 32: compare before and after feature scaling."""
from _common import linear, split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
m,_,xt,_,yt=linear(); xtr,xt2,ytr,yt2=split(); sm=make_pipeline(StandardScaler(),LinearRegression()).fit(xtr,ytr); print({'before':m.score(xt,yt),'after':sm.score(xt2,yt2)})
