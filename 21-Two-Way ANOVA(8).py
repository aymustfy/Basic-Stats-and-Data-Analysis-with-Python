import pandas as pd
import statsmodels.api as sm
import statsmodels.stats as ss
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from scipy import stats

data=pd.read_excel("C:/Users/MSTF/Desktop/Basic Statistic/8.xlsx")
data2=data.copy()

model=ols("Performance ~ C(Position) + C(WorkingDuration) + C(Position) : C(WorkingDuration)",data=data2).fit()
errors=model.resid

normality=stats.shapiro(errors)
print(normality)

fig=sm.qqplot(errors,line="s")
plt.show()

print(model.summary())
#Prof(F-statistic)<0.05 Model is meaningful.

anova=sm.stats.anova_lm(model,type=2)
print(anova)
#Positions have an impact on performance. WorkingDuration have not enough impact on performance. Positions and working duration together impact on performance.


#For position
positfact=ss.multicomp.pairwise_tukeyhsd(endog=data2["Performance"],groups=data2["Position"])
print(positfact)
# If reject=True is meaningful between groups.

group1=data2.groupby("Position")["Performance"].mean()
print(group1)
# Mean is calculated for all groups.

#For position and working duration
positduratfact=ss.multicomp.pairwise_tukeyhsd(endog=data2["Performance"],groups=data2["Position"]+data2["WorkingDuration"])
print(positduratfact)
# If reject=True is meaningful between groups.

group2=data2.groupby(["Position","WorkingDuration"]).mean()
print(group2)
# Mean is calculated for all posit-duration groups.
# For Workers, performance declines as time goes on. 
# Performance drops slightly as time increases for Journeymans.
# For Managers, the longer the time, the higher the performance.
