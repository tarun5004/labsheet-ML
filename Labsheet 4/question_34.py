"""Question 34: save a trained model with Joblib."""
import joblib
from _common import OUTPUT_DIR, linear
model,*_=linear(); OUTPUT_DIR.mkdir(exist_ok=True); joblib.dump(model,OUTPUT_DIR/'regression_model.joblib'); print('model saved')
