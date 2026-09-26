"""Question 31: train with standardized features."""
from _common import split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
xtr,xt,ytr,yt=split(); model=make_pipeline(StandardScaler(),LinearRegression()).fit(xtr,ytr); print(model.score(xt,yt))
