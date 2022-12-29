import pandas as pd
import pingouin as pg
from statsmodels.multivariate.manova import MANOVA

data=pd.read_excel("C:/Users/MSTF/Desktop/Basic Statistic/10.xlsx")
data2=data.copy()

homogeneity=pg.homoscedasticity(data2,dv="WomanAttitude",group="Product",center="mean")
homogeneity2=pg.homoscedasticity(data2,dv="ManAttitude",group="Product",center="mean")
print(homogeneity,homogeneity2)
#if pval>0.05, equal_var=True Homogeneity H0 can't deny.

varcov=pg.box_m(data2,dvs=["ManAttitude","WomanAttitude"], group="Product")
print(varcov)
#varcovarians matris equality pval>0.05 

model=MANOVA.from_formula("ManAttitude+WomanAttitude~Product",data=data2)
print(model.mv_test())
# Pr>F < 0.05 for Wilks' lambda test. This results meaningful.

posthoc1=pg.pairwise_tukey(data=data2,dv="ManAttitude",between="Product")
posthoc2=pg.pairwise_tukey(data=data2,dv="WomanAttitude",between="Product")

print(posthoc1,posthoc2)

# While the attitude difference is invisible for men, 
# there is an attitude difference between product1-product3 and product2-product3 for women because the p-tukey test is less than 0.05.