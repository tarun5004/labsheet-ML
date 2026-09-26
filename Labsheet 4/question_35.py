"""Question 35: load a saved model and predict."""
import joblib
from _common import OUTPUT_DIR, data
model_path=OUTPUT_DIR/'regression_model.joblib'
if not model_path.exists():
 from _common import linear
 model,*_=linear(); OUTPUT_DIR.mkdir(exist_ok=True); joblib.dump(model,model_path)
model=joblib.load(model_path); print(model.predict(data()[0].head()))
