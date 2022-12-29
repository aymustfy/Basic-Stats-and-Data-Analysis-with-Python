import pandas as pd
from scipy import stats

data=pd.read_excel("C:/Users/MSTF/Desktop/Basic Statistic/13.xlsx")
data2=data.copy()

table=pd.crosstab(index=data2["Gender"],columns=data2["Hand"])
print(table)

#Chi-square test selection based on expected value
test,p,sd,exp=stats.chi2_contingency(table)
print(exp)

# If exp>25 Pearson chisquare, 
# If 5<exp<25 Yates chisquare, 
# If exp<5 Fisher chisquare

#Pearson chisquare
test,p,sd,exp=stats.chi2_contingency(table,correction=False)
print(test,p)

#Yates chisquare(Selected)
test2,p2,sd,exp=stats.chi2_contingency(table,correction=True)
print(test2,p2)

#Fisher chisquare
test=stats.fisher_exact(table)
print(test)


