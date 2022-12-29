from scipy import stats

#If there is an average of 6 earthquakes in a year;

#1-probability of 3 earthquake
#2-probability of at most 3 earthquakes

mean=6
distrib=stats.poisson(mean)

prob1=distrib.pmf(k=3)
prob2=distrib.cdf(x=3)

print(prob1,prob2)