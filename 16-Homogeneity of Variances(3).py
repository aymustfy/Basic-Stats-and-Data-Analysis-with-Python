import pandas as pd
from scipy import stats


data=pd.read_excel("C:/Users/MSTF/Desktop/Basic Statistic/3.xlsx")
print(data)

man=data[data["Gender"]=="Man"]
woman=data[data["Gender"]=="Woman"]

p1=stats.shapiro(man["Spending"])
p2=stats.shapiro(woman["Spending"])

print(p1)
print(p2)

h1=stats.levene(man["Spending"],woman["Spending"],center="mean")
h2=stats.bartlett(man["Spending"],woman["Spending"])

print(h1)
print(h2)

#if pvalue>alpha H0 not denied,
#if pvalue<alpha H0 denied.