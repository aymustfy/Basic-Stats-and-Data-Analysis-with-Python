import pandas as pd
import pingouin as pg
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_excel("C:/Users/MSTF/Desktop/Basic Statistic/21.xlsx")
data2=data.copy()

cormat=data2.corr()

sns.heatmap(cormat,annot=True,cmap=plt.cm.Blues)
plt.show()

p1=pg.pairwise_corr(data2)
print(p1)

p2=pg.rcorr(data2,stars=False)
print(p2)

#A-C and A-D relations have meaningful correlation. Correlation coefficent(r) 0,53 between A and C. For A and D r=-0,427 so negative correlation.
