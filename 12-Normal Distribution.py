from scipy import stats
import numpy as np

#If a bus arrives at a stop every 15 minutes,

#1-Average waiting time?
#2-Less than 12.5 minute waiting time?
mean=500
var=100
distrib=stats.norm(mean,np.sqrt(var))

prob1=distrib.cdf(x=518)

prob2=distrib.sf(x=518)

print(prob1,prob2)