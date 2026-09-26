"""Question 31: extract year, month, and day from a date."""
from _common import dataset
frame=dataset(); frame['year']=frame.date.dt.year; frame['month']=frame.date.dt.month; frame['day']=frame.date.dt.day; print(frame[['date','year','month','day']].head())
