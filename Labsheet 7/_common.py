"""Shared helpers for supervised-learning mini projects."""
from pathlib import Path
import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import make_regression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score, accuracy_score
from sklearn.preprocessing import StandardScaler

LAB_DIR = Path(__file__).parent
OUTPUT_DIR = LAB_DIR / 'outputs'

def student_data(seed=42):
    rng=np.random.default_rng(seed); n=240
    frame=pd.DataFrame({'attendance':rng.uniform(55,100,n),'internal_marks':rng.uniform(35,95,n),'assignments':rng.uniform(30,100,n),'study_hours':rng.uniform(1,12,n),'previous_result':rng.uniform(35,95,n)})
    frame['performance']=.25*frame.attendance+.3*frame.internal_marks+.15*frame.assignments+1.5*frame.study_hours+.3*frame.previous_result+rng.normal(0,4,n)
    return frame

def house_data(seed=42):
    x,y=make_regression(n_samples=240,n_features=5,n_informative=5,noise=12,random_state=seed)
    frame=pd.DataFrame(x,columns=['area','bedrooms','location_score','bathrooms','age']); frame['price']=y*1000+250000; return frame

def regression_models(frame,target):
    x_train,x_test,y_train,y_test=train_test_split(frame.drop(columns=target),frame[target],test_size=.2,random_state=42)
    models={'linear':LinearRegression(),'forest':RandomForestRegressor(n_estimators=80,random_state=42)}
    return x_train,x_test,y_train,y_test,models

def save_plot(name):
    OUTPUT_DIR.mkdir(exist_ok=True); path=OUTPUT_DIR/name; plt.tight_layout(); plt.savefig(path,dpi=140); plt.close(); return path
