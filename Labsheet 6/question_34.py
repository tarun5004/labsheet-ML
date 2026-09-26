"""Question 34: analyze hyperparameter impact."""
from _common import train
for params in ({'alpha':.05},{'alpha':.3},{'gamma':.8},{'gamma':.99},{'epsilon':.5}): print(params,train(300,**params)[2][-30:].mean())
