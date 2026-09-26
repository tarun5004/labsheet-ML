"""Question 35: save a final preprocessed dataset."""
from _common import dataset, save
frame=dataset().drop(columns='date'); frame=__import__('pandas').get_dummies(frame, columns=['species']); print(save(frame, 'final_preprocessed.csv'))
