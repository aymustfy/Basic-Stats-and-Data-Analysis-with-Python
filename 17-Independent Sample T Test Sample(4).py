import pandas as pd
from scipy import stats

#When we work on the data obtained as a result of a survey to measure the consumer attitude that occurs with the innovation of the beverage company on a product;

data=pd.read_excel("C:/Users/MSTF/Desktop/Basic Statistic/4.xlsx")
data2=data.copy()

old=data2[data2["Group"]=="Old"]
new=data2[data2["Group"]=="New"]

normold=stats.shapiro(old["Attitude"])
normnew=stats.shapiro(new["Attitude"])

print(normold,normnew)

homogeneity=stats.bartlett(old["Attitude"],new["Attitude"])
print(homogeneity)

test=stats.ttest_ind(old["Attitude"],new["Attitude"],alternative="two-sided")
print(test)

print(old["Attitude"].mean())
print(new["Attitude"].mean())

#New beverage disliked.

#if Bartlett's result pValue<alpha;
test=stats.ttest_ind(old["Attitude"],new["Attitude"],alternative="two-sided",equal_var=False)

