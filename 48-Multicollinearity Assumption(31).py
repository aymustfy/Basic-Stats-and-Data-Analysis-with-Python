import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.outliers_influence import variance_inflation_factor

data=pd.read_excel("C:/Users/MSTF/Desktop/Basic Statistic/31.xlsx")
data2=data.copy()

x=data2[["X1","X2","X3","X4","X5","X6","X7","X8","X9","X10"]]
y=data2["Y"]

constant=sm.add_constant(x)
model=sm.OLS(y,constant).fit()
print(model.summary())

correlation=x.corr()
sns.heatmap(data=correlation,annot=True,fmt=".2f")
plt.show()

vif=pd.DataFrame()
vif["Variables"]=x.columns
vif["VIF"]=[variance_inflation_factor(constant.values,i+1) for i in range(x.shape[1])]
print(vif)

# Multicollinearity is high for values greater than 5 in the results.
# To solve the problem, it is necessary to discard the variable with the highest vif value and have it calculated again. 
# Maximum values are thrown one by one until the desired level is reached.

x=data2[["X1","X3","X4","X5","X6","X7","X8","X9","X10"]]
y=data2["Y"]

constant=sm.add_constant(x)
model=sm.OLS(y,constant).fit()
print(model.summary())

correlation=x.corr()
sns.heatmap(data=correlation,annot=True,fmt=".2f")
plt.show()

vif=pd.DataFrame()
vif["Variables"]=x.columns
vif["VIF"]=[variance_inflation_factor(constant.values,i+1) for i in range(x.shape[1])]
print(vif)

# After the X2 variable with the highest vif value was excluded from the model, 
# The other values greater than 5 also decreased below 5 and the multicollinearity problem in the model was resolved.