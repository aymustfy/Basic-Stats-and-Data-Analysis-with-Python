import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

np.random.seed(0)
data=np.random.normal(35,2,20)
datacopy=data.copy()

data1=stats.t.rvs(loc=0,df=1,size=15)
data2=stats.t.rvs(loc=0,df=5,size=15)
data3=stats.t.rvs(loc=0,df=20,size=15)

sns.distplot(data1,hist=False,color="red")
sns.distplot(data2,hist=False,color="green")
sns.distplot(data3,hist=False,color="blue")

plt.show()

