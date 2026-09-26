"""Question 33: apply a log transformation."""
import numpy as np
from _common import dataset
frame=dataset(); frame['log_sepal_length']=np.log1p(frame.sepal_length); print(frame[['sepal_length','log_sepal_length']].head())
