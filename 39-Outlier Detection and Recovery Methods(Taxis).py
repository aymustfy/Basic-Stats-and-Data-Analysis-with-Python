import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.neighbors import LocalOutlierFactor

data=sns.load_dataset("taxis")
data2=data.copy()

### Outlier Detection
outlier=pd.DataFrame(data=data2,columns=["fare","tip"])
LOF=LocalOutlierFactor(n_neighbors=20,contamination=0.1)
predict=LOF.fit_predict(outlier)
print(outlier[predict==-1])
sns.scatterplot(data=data2,x="fare",y="tip")
plt.show()

sns.boxplot(data=data2["tip"])
plt.show()
### Outlier Detection

### Calculating Outlier Limits and Listing Them
q1=data2["tip"].quantile(0.25)
q3=data2["tip"].quantile(0.75)
IQR=q3-q1

Lowerlimit=q1-1.5*IQR
Upperlimit=q1+1.5*IQR

Outliermin=data2.loc[data2["tip"]<Lowerlimit]["tip"]
Outliermax=data2.loc[data2["tip"]>Upperlimit]["tip"]

Outlier=pd.concat([Outliermin,Outliermax],axis=0).index

indexes=[]

for i in Outlier:
    indexes.append(i)

### Calculating Outlier Limits and Listing Them

#### 1-Outlier values can clean on dataset
data3=data2.drop(data2.index[indexes])
sns.boxplot(data=data3["tip"])
plt.show()

#### 2-Outlier values can fill as mean of values
mean=data2["tip"].mean()
data2.loc[indexes,"tip"]=mean
sns.boxplot(data=data2["tip"])
plt.show()

#### 3-Outlier values can fill as min-max values
data2.loc[data2["tip"]<Lowerlimit]["tip"]=Lowerlimit
data2.loc[data2["tip"]>Upperlimit]["tip"]=Upperlimit
sns.boxplot(data=data2["tip"])
plt.show()