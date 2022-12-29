import seaborn as sns
import matplotlib.pyplot as plt

data=sns.load_dataset("titanic")
data2=data.copy()

data2["age"].fillna(data2.groupby("sex")["age"].transform("mean"),inplace=True)

sns.boxplot(data=data2["age"])
plt.show()

q1=data2["age"].quantile(0.25)
q3=data2["age"].quantile(0.75)

IQR=q3-q1

LowerLimit=q1-1.5*IQR
UpperLimit=q1+1.5*IQR

Under_LL=data2[data2["age"]<LowerLimit]["age"]
Over_UL=data2[data2["age"]>UpperLimit]["age"]

print("Under Lower Limit",Under_LL, "\n\n","Over Upper Limit",Over_UL)
