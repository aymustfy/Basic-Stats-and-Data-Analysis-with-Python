from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(10)
data=stats.norm.rvs(loc=38,size=500)

print("Kurtosis result:",stats.kurtosis(data))
print("Skewness result:",stats.skew(data))
##-1.5<results<1.5     ====>  normal

stats.probplot(data,dist="norm",plot=plt)
plt.show()

#kolmogorov-smirnow single sample test
ks=stats.kstest(data,cdf="norm",args=(data.mean(),data.std()))
print("Smirnow test result:" f"{ks.pvalue:5f}")

#shapiro-wilk sample test
sw=stats.shapiro(data)
print("Shapiro test result:" f"{sw.pvalue:5f}")