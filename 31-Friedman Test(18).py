import pandas as pd
import pingouin as pg
from scikit_posthocs import posthoc_conover_friedman
import numpy as np

data=pd.read_excel("C:/Users/MSTF/Desktop/Basic Statistic/18.xlsx")
data2=data.copy()

data3=pd.melt(data2,id_vars=["Patients"],value_vars=["Before Treatment","After Treatment","After Treatment 2","After Treatment 3"])
data3.columns=["Patients","Tests","Values"]

normality=pg.normality(data3,dv="Values",group="Tests")
print(normality)

test=pg.friedman(data3,dv="Values",within="Tests",subject="Patients")
print("\n",test)
# Since p-unc>0.05, it will be said that there is no relationship in fact. 
# However, under the assumption that there is a relationship, the posthoc is created as follows.

df=np.array([data2["Before Treatment"],data2["After Treatment"],data2["After Treatment 2"],data2["After Treatment 3"]])
posthoc=posthoc_conover_friedman(df,p_adjust="bonf")
print("\n",posthoc)

# The results show us that there was no difference between the groups. We have verified the above test.