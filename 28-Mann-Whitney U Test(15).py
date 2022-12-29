
import pandas as pd
import pingouin as pg

data=pd.read_excel("C:/Users/MSTF/Desktop/Basic Statistic/15.xlsx")
data2=data.copy()

normality=pg.normality(data2,dv="Duration",group="Gender")
print(normality)
#Distribution for Woman Normal, Man not normal. So we need to apply non-parametric test.

man=data2[data2["Gender"]=="Man"]["Duration"]
woman=data2[data2["Gender"]=="Woman"]["Duration"]

test=pg.mwu(man,woman,alternative="two-sided") #Alternative could be "greater" or "less". But we need to detect difference between gender groups. 
#So we use the two-sided.

print(test)
#if p>0.05 H0 can't deny. These results show us that the duration is not different for man and woman.

