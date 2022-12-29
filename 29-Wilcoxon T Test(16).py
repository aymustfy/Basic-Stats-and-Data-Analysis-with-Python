import pandas as pd
import pingouin as pg

data=pd.read_excel("C:/Users/MSTF/Desktop/Basic Statistic/16.xlsx")
data2=data.copy()

difference=data2["Before Treatment"]-data2["After Treatment"]
normality=pg.normality(difference)
print(normality)
#Distribution is not normal. So we need to apply nonparametric test(wilcoxon).

test=pg.wilcoxon(data2["Before Treatment"],data2["After Treatment"],alternative="two-sided")
print(test)
#if p>0.05 H0 can't deny. 