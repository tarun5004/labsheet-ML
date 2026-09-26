"""Question 30: combine two existing columns into a feature."""
from _common import dataset
frame=dataset(); frame['sepal_area']=frame.sepal_length*frame.sepal_width; print(frame[['sepal_length','sepal_width','sepal_area']].head())
