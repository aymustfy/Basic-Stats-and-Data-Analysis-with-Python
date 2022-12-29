import pandas as pd
from scipy import stats
from statsmodels.stats.descriptivestats import sign_test

data=pd.read_excel("C:/Users/MSTF/Desktop/Basic Statistic/14.xlsx")
data2=data.copy()

#H0 hip median=30
norm=stats.shapiro(data2["Score"])
print(norm)


test=sign_test(data2["Score"],mu0=30)
print(test)
# If p>0.05 H0 can't deny. 
# Test results p<0.05 H0 denied.

print(data2["Score"].median())
