import pandas as pd
from scipy import stats

#Under the assumption that when evaluating past data in an exam, it is understood that the average is 28;

#If it is discussed whether the new education method makes a difference based on the grades of 12 randomly selected 
#students with the education method that was reorganized this year; (confidence interval=0,95)

#H0--> M=28
#H1--> M!=28

data=pd.read_excel("C:/Users/MSTF/Desktop/Basic Statistic/1.xlsx")
alpha=0.05

thesap,p=stats.ttest_1samp(data,popmean=28,alternative="two-sided")
print(thesap,p)

if p<alpha:
    print("H0 Denied")
else:
    print("H0 Not Denied")

#H0 Denied, new education method has made a difference in exam grades compared to the old one.