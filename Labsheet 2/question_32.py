"""Question 32: create a mathematically transformed feature."""
import numpy as np
from _common import dataset
frame=dataset(); frame['petal_area']=frame.petal_length*frame.petal_width; frame['sqrt_area']=np.sqrt(frame.petal_area); print(frame[['petal_area','sqrt_area']].head())
