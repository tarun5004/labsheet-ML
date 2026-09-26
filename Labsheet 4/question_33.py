"""Question 33: perform regression on another real-world dataset."""
from sklearn.datasets import load_linnerud
from sklearn.linear_model import LinearRegression
x,y=load_linnerud(return_X_y=True); model=LinearRegression().fit(x,y[:,0]); print(model.score(x,y[:,0]))
