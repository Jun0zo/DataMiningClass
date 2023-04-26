import matplotlib.pyplot as plt
import pandas as pd
from EM import EM

csv = pd.read_csv("data.csv", sep="\t")
data = csv.iloc[:,0:2].values.tolist()

em = EM(data=data, K=3)
em.clustering()
em.plotting()