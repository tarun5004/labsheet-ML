"""Question 29: binary encode category codes."""
from sklearn.preprocessing import LabelEncoder
from _common import dataset
frame=dataset(); codes=LabelEncoder().fit_transform(frame.species); frame['binary_code']=[format(code,'02b') for code in codes]; print(frame[['species','binary_code']].head())
