"""Question 17: cap values at the 1st and 99th percentiles."""
from _common import dataset, numeric
frame=dataset(); values=numeric(frame); frame[values.columns]=values.clip(values.quantile(.01), values.quantile(.99), axis=1); print(frame[values.columns].describe().loc[['min','max']])
