from scipy import stats

#If a bus arrives at a stop every 15 minutes,

#1-Average waiting time?
#2-Less than 12.5 minute waiting time?
a=0
b=15
distrib=stats.uniform(a,b)

prob1=distrib.expect()

prob2=distrib.cdf(x=12.5)

print(prob1,prob2)