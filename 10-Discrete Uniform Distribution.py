from scipy import stats

#when a dice is rolled;
#1-probability of getting 1
#2-3 or less probability

n=6
distrib=stats.randint(1,n+1)

prob1=distrib.pmf(k=1)
varn=distrib.var()

exp=distrib.expect()
prob2=distrib.cdf(x=3)

print(prob1,prob2)