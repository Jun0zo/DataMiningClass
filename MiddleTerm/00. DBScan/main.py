import matplotlib.pyplot as plt
import pandas as pd
from DBScan import DBScan

csv = pd.read_csv("data.csv", sep="\t")
data = csv.iloc[:,0:2].values.tolist()

# X = [d[0] for d in data]
# Y = [d[1] for d in data]
# plt.scatter(X, Y)
# plt.show()

dbscan = DBScan(data=data)

dbscan.plotting()
dbscan.clustering()
dbscan.plotting()