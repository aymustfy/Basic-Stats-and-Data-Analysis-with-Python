import pandas as pd
import pingouin as pg

data=pd.read_excel("C:/Users/MSTF/Desktop/Basic Statistic/22.xlsx")
data2=data.copy()

corr=pg.pairwise_corr(data2)
print(corr)
# A significant correlation was found between all variables.

partcorr=pg.partial_corr(data=data2,x="Repast",y="Weight",covar="Age")
print(partcorr)

# In this case, in order to obtain the correlation relationship between repast and weight, the direct correlation between repast and weight can be found by excluding the age variable with the code above. 
# Here, the correlation coefficient, which was 0.87 at the beginning, decreased to 0.63. 
# In other words, the difference is the effect of the age variable.