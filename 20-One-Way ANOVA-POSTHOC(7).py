import pandas as pd
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import pingouin as pg
import scikit_posthocs as sp

data=pd.read_excel("C:/Users/MSTF/Desktop/Basic Statistic/7.xlsx")
data2=data.copy()

g1=data2[data2["Education"]=="Primary School"]
g2=data2[data2["Education"]=="High School"]
g3=data2[data2["Education"]=="University"]
g4=data2[data2["Education"]=="Master"]

normality1=stats.shapiro(g1["Tv"])
normality2=stats.shapiro(g2["Tv"])
normality3=stats.shapiro(g3["Tv"])
normality4=stats.shapiro(g4["Tv"])

print("Primary School",normality1,"\nHigh School",
normality2,"\nUniversity",normality3,"\nMaster",normality4)

homogeneity=stats.bartlett(g1["Tv"],g2["Tv"],g3["Tv"],g4["Tv"])
print(homogeneity)

testanova=stats.f_oneway(g1["Tv"],g2["Tv"],g3["Tv"],g4["Tv"])
print(testanova)

# There is a difference between the duration of watching TV according to the level of education.
# However, this test does not tell which groups there is a difference. This requires post-hoc analysis.

posthoc=pairwise_tukeyhsd(data2["Tv"],data2["Education"], alpha=0.5)
print(posthoc)

test=pg.welch_anova(data=data2,dv="Tv",between="Education")
print(test)

tamhane=sp.posthoc_tamhane(data2,val_col="Tv",group_col="Education")
print(tamhane)

#There is a significant difference between the education levels of Master-Primary School and Master-University in terms of television viewing time.