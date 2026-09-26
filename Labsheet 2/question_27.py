"""Question 27: label encode a categorical variable."""
from sklearn.preprocessing import LabelEncoder
from _common import dataset
frame=dataset(); frame['species_code']=LabelEncoder().fit_transform(frame.species); print(frame[['species','species_code']].head())
