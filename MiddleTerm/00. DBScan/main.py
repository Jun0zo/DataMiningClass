import matplotlib.pyplot as plt
import pandas as pd
from DBSCAN import DBSCAN

csv = pd.read_csv("data.csv", sep="\t")
data = csv.iloc[:,0:2].values.tolist()

dbscan = DBSCAN(data=data)

dbscan.plotting()
dbscan.clustering()
dbscan.plotting()