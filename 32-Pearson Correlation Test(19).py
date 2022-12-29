import pandas as pd
import pingouin as pg
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_csv("C:/Users/MSTF/Desktop/Basic Statistic/19.csv")
data2=data.copy()

normality=pg.normality(data2)
print(normality)

sns.lmplot(x="Temperature",y="Revenue",data=data2,ci=None)
plt.show()

correlation=pg.corr(data2["Temperature"],data2["Revenue"],method="pearson")
print(correlation)

#r=0.989. So there is shows us strong positive correlation between Temperature and Ice-Cream Revenue.