"""Question 14: train multiple linear regression."""
from _common import linear
model,x_train,*_=linear(); print(model.score(x_train, _[-1]) if False else 'model trained')
