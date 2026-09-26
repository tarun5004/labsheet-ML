"""Question 34: save the clustered dataset."""
from _common import data, kmeans, save_plot, OUTPUT_DIR
frame=data(); frame['cluster']=kmeans().labels_; OUTPUT_DIR.mkdir(exist_ok=True); frame.to_csv(OUTPUT_DIR/'clustered_iris.csv',index=False); print('clustered_iris.csv saved')
