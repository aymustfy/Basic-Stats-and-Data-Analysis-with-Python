import pandas as pd
from scipy import stats

# If the excel exam scores made before and after the excel training in the company are evaluated;
data=pd.read_excel("C:/Users/MSTF/Desktop/Basic Statistic/5.xlsx")
data2=data.copy()

before=data2["Before"]
after=data2["After"]
difference=before-after

normality=stats.shapiro(difference)
print(normality)
#p value>0.05 normal

var_homogeneity=stats.bartlett(before,after)
print(var_homogeneity)
#p value>0.05 homogeneous

t,p=stats.ttest_rel(before,after,alternative="two-sided")
print("Test Result=%.4f,p-Value=%.4f"%(t,p))
#p value<0.05 H0 denied.
