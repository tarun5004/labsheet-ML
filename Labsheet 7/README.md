# Lab Sheet 07: Unsupervised Learning Applications

This lab contains two beginner-friendly mini projects. Both projects create
small reproducible datasets, so they can be demonstrated without downloading
data during the viva.

## Requirements

From the repository root, install the dependencies once:

```powershell
python -m pip install -r requirements.txt
```

## Project 1: Customer Segmentation

Features: age, annual income, spending score, and purchases per year.

```powershell
python "Labsheet 7\project_01_customer_segmentation\customer_segmentation.py"
```

The script scales the features, selects `k` using the silhouette score, then
compares K-Means with hierarchical clustering. It saves a CSV and two PCA
visualizations in the project's `outputs` folder.

## Project 2: News Article Clustering

The script converts article text into TF-IDF features, selects the number of
clusters, and compares K-Means with hierarchical clustering.

```powershell
python "Labsheet 7\project_02_news_clustering\news_clustering.py"
```

It prints evaluation scores and important words for each cluster, then saves
the clustered articles and two visualizations in the project's `outputs`
folder.

## Viva points

- Unsupervised learning finds groups without a target label.
- StandardScaler prevents a large-valued feature from dominating distance.
- TF-IDF gives more weight to words that are useful for distinguishing articles.
- A higher silhouette score generally means better-separated clusters.