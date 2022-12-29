import pandas as pd
from scipy import stats

data=pd.read_excel("C:/Users/MSTF/Desktop/Basic Statistic/12.xlsx")
data2=data.copy()

frequency=pd.value_counts(data2["Weight"])
print(frequency)

chisqu,p=stats.chisquare(frequency)
print(chisqu,p)

#Since p>0.05, there is no difference between the observed value and the expected value.