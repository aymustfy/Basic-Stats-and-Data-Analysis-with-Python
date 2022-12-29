from scipy import stats

#In a store where 10 out of 100 sales per week are returned, the number of returns in 50 sales per week;

#1-5 probability of return
#2-Probability of less than 15 returns
#3-The probability of getting more than 10 returns

p=0.1
n=50
distrib=stats.binom(n,p)

prob1=distrib.pmf(k=5)
prob2=distrib.cdf(x=15)
prob3=1-distrib.cdf(x=10)

print(prob1,prob2,prob3)