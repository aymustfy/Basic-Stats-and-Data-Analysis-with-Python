import pandas as pd
import pingouin as pg
from scikit_posthocs import posthoc_conover

data=pd.read_excel("C:/Users/MSTF/Desktop/Basic Statistic/17.xlsx")
data2=data.copy()

data3=pd.melt(data2,value_vars=["Method A","Method B","Method C"])
data3.columns=["Method","Value"]

normality=pg.normality(data3,dv="Value",group="Method")
print(normality)

test=pg.kruskal(data3,dv="Value",between="Method")
print(test)

#if normality p<0.05 non-parametric tests apply.
#if test result p-unc<0.05 H0 deny.
#There is a difference between groups. Posthoc applied to detect, which groups differed. 

posthoc=posthoc_conover(data2,val_col="Value",group_col="Method",p_adjust="bonf")
print(posthoc)

