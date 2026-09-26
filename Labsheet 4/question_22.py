"""Question 22: predict with polynomial regression."""
from _common import polynomial
model,*_=polynomial(2); print(model.predict(_[1].head()) if False else model.predict(polynomial(2)[2].head()))
