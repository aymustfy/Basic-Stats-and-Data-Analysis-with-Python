import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.stats.diagnostic as dg
import numpy as np
from statsmodels.stats.outliers_influence import variance_inflation_factor

data=pd.read_csv("C:/Users/MSTF/Desktop/Basic Statistic/30.csv")
data2=data.copy()

x=data2[["TV","Radio","Newspaper"]]
y=data2["Sales"]

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