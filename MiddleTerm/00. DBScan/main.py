import pandas as pd
from DBScan import DBScan

data = pd.read_csv("data.csv", sep="\t").values.tolist()
# dbscan = DBScan(data=data)
# dbscan.clustering()

print(data)