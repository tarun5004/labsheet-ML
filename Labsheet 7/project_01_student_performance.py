"""Project 1: student performance prediction system."""
import joblib
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, r2_score
from _common import student_data, regression_models, OUTPUT_DIR, save_plot

frame=student_data(); xtr,xt,ytr,yt,models=regression_models(frame,'performance'); results={}
for name,model in models.items():
    model.fit(xtr,ytr); prediction=model.predict(xt); results[name]={'MAE':mean_absolute_error(yt,prediction),'R2':r2_score(yt,prediction)}
    if name=='forest': OUTPUT_DIR.mkdir(exist_ok=True); joblib.dump(model,OUTPUT_DIR/'student_performance_model.joblib'); plt.scatter(yt,prediction); plt.xlabel('Actual'); plt.ylabel('Predicted'); save_plot('student_performance_predictions.png')
frame.to_csv(OUTPUT_DIR/'student_performance_dataset.csv',index=False); print(results)
