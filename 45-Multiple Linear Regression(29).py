import statsmodels.api as sm
import pandas as pd

data=pd.read_excel("C:/Users/MSTF/Desktop/Basic Statistic/29.xlsx")
data2=data.copy()

x=data2[["Chicken Price","Income","Beef Price"]]
y=data2["Chicken Consumption"]

constant=sm.add_constant(x)
model=sm.OLS(y,constant).fit()
print(model.summary())

# Adj. R-squared is the value to be considered in multiple linear regression.
# It is the value that must be read so that the variables that do not contribute to the explanatory power of the model are not included in the model.