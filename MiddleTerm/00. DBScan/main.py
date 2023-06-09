import pandas as pd
from DBSCAN import DBSCAN

csv = pd.read_csv("data2.csv", sep="\t")
data = csv.iloc[:,0:2].values.tolist()

dbscan = DBSCAN(data=data, eps=0.12, min_pts=2)

# dbscan.plotting()
dbscan.clustering()
dbscan.plotting()