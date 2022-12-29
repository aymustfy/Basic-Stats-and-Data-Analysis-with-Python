import pandas as pd
import pingouin as pg
from statsmodels.multivariate.manova import MANOVA

data=pd.read_excel("C:/Users/MSTF/Desktop/Basic Statistic/11.xlsx")
data2=data.copy()

model=MANOVA.from_formula("Performance+Affiliation~Position+Departmant+Position:Departmant",data=data2)
print(model.mv_test())

#Position affected performance, Departmant not affected performance and affiliation,
# Position and Departmant affected performance

posthoc1=pg.pairwise_tukey(data=data2,dv="Performance",between="Position")
posthoc2=pg.pairwise_tukey(data=data2,dv="Affiliation",between="Position")

print(posthoc1,"\n",posthoc2)

# While there is no significant performance difference between Manager and Manager positions, there are for the other two comparisons.

# There are differences between all positions for Affiliation.