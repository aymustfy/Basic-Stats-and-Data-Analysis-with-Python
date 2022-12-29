from scipy import stats

#By exemplifying the probability of the king coming on the playing card,
p=4/52
distrib=stats.bernoulli(p)

king=distrib.pmf(k=1)
noking=distrib.pmf(k=0)

print(king,noking)
print(distrib.expect())
print(distrib.var())
#By exemplifying the probability of the king coming on the playing card,
