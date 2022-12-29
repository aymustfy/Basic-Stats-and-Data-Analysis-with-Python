import numpy as np
from scipy import stats

#standard deviation is known, normal distribution, mean confidence interval
n=100
xmean=1040
xstd=25
alpha=0.95

interval=stats.norm.interval(alpha=alpha,loc=xmean,scale=xstd/np.sqrt(n))

print(interval)
#standard deviation is known, normal distribution, mean confidence interval

#standard deviation is unknown, t distribution, mean confidence interval
n=30
mean=140
std=25
alpha=0.95
degfreed=n-1
interval2=stats.t.interval(alpha=alpha,loc=mean,df=degfreed,scale=std/np.sqrt(n))
print(interval2)
#standard deviation is unknown, t distribution, mean confidence interval

#Confidence Interval of the Mean Difference between two populations
na=8
nb=10
vara=196
varb=144
meana=182
meanb=176
alpha=0.95
interval3=stats.norm.interval(alpha=alpha,loc=(meana-meanb),scale=np.sqrt((vara/na)+(varb/nb)))
print(interval3)
#Confidence Interval of the Mean Difference between two populations