import pandas as pd
import numpy as np
from EM import EM

x = np.random.normal(7, 3, size=10)
y = np.random.normal(20, 3, size=10)
data = np.concatenate([x, y]).tolist()

print('x :', x)
print('y : ', y)
em = EM(data=data)
em.clustering()