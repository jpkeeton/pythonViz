# from  https://seaborn.pydata.org/generated/seaborn.heatmap.html

import numpy as np; np.random.seed(0)
import seaborn as sns; sns.set()
uniform_data = np.random.rand(10, 12)
ax = sns.heatmap(uniform_data)