import pandas as pd
from statsmodels.stats.proportion import proportions_ztest
# In order to understand the importance of the website design in product sales, 
# under the assumption that the change in the sales amount is desired to be examined when the new and old design is presented to the users for 30 days;

data=pd.read_excel("C:/Users/MSTF/Desktop/Basic Statistic/6.xlsx")
data2=data.copy()

table=pd.crosstab(data2["Group"],data2["Website"])
#print(table)

Control=data2[data2["Group"]=="Control"].sample(n=5000,random_state=42)
Experimental=data2[data2["Group"]=="Experimental"].sample(n=5000,random_state=42)

#print(Control.count(),Experimental.count())

datanew=pd.concat([Control,Experimental],axis=0)
datanew.reset_index(drop=True,inplace=True)

#print(datanew)

Groupby=datanew.groupby("Group")["Sales"]
#print(Groupby.mean())

Control2=datanew[datanew["Group"]=="Control"]["Sales"]
Experimental2=datanew[datanew["Group"]=="Experimental"]["Sales"]

Achieve=[Control2.sum(),Experimental2.sum()]
Observation=[Control2.count(),Experimental2.count()]

test,p=proportions_ztest(Achieve,Observation,alternative="two-sided")
print("Test Results: {}   P-Value: {}".format(test,p))

# P-Value>0.05 
# H0 can't deny. It was found that there was no significant difference between the new design and the old design.
