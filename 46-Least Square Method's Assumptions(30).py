import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.stats.diagnostic as dg
import numpy as np

data=pd.read_csv("C:/Users/MSTF/Desktop/Basic Statistic/30.csv")
data2=data.copy()
# Linearity Assumption
sns.pairplot(data=data2,y_vars="Sales",x_vars=["TV","Radio","Newspaper"],kind="reg")
plt.show()

x=data2[["TV","Radio","Newspaper"]]
y=data2["Sales"]

constant=sm.add_constant(x)
model=sm.OLS(y,constant).fit()
print(model.summary())

# Normality Assumption
sm.qqplot(model.resid,line="s")
plt.show()

sns.distplot(model.resid,kde=True)
plt.show()

# Autocorrelation Assumption
mistake=model.resid
sm.graphics.tsa.plot_acf(mistake)
plt.show()
#In the resulting graph, there is no autocorrelation since the values are in the horizontal area.

lm=dg.acorr_breusch_godfrey(model,nlags=2)
print(lm)

# If there was an autocorrelation problem, the Neney-West Estimator as below would be used.
model2=sm.OLS(y,constant).fit(cov_type="HAC",cov_kwds={"maxlags":3})
print(model2.summary())
# If Durbin-Watson is between 1,5 and 2,5 there is no autocorrelation problem

# Constant Variance Assumption
error=model.resid
whitetest=dg.het_white(error,model.model.exog)
print(whitetest)
# If prob(F)<0.05; H0 denied. Non-constant variance

BPTest=dg.het_breuschpagan(error,model.model.exog)
print(BPTest)
# prob(F)>0.05; H0 can't deny. Constant variance

# If it is not constant variance, log model transformation is performed.
