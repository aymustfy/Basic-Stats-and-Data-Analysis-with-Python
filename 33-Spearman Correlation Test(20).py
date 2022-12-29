import pandas as pd
import pingouin as pg
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_excel("C:/Users/MSTF/Desktop/Basic Statistic/20.xlsx")
data2=data.copy()

normality=pg.normality(data2)
print(normality)

sns.lmplot(x="A",y="B",data=data2)
plt.show()

score=pg.corr(data2["A"],data2["B"],method="spearman")
print(score)

#r=-0.918. So there is shows us strong negative correlation between A and B.