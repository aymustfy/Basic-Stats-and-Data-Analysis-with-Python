import seaborn as sns
import statsmodels.api as sm

data=sns.load_dataset("tips")
data2=data.copy()

constant=sm.add_constant(data2["total_bill"])
dependentvariable=data2["tip"]

model=sm.OLS(dependentvariable,constant).fit()
print(model.summary())

# If prob(f-stat)<0,05 ; model is meaningfull. H0 deny. Else model is meaningless. H0 can't deny.
# If P>|t| < 0.05 ; parameters is meaningfull. H0 deny. Else parameter is meaningless. H0 can't deny.
# R-squared shows the descriptiveness of the model. 