import pandas as pd
from scipy import stats

#It is desired to compare the exam results of the students from two different schools over the averages. 
#Under the assumption that 9 students were randomly selected, considering that other assumptions were also met;
#H0--> Ma=Mb
#H1--> Ma!=Mb

data=pd.read_excel("C:/Users/MSTF/Desktop/Basic Statistic/2.xlsx")

alpha=0.05

thesap,p=stats.ttest_ind(data["School A"],data["School B"],alternative="two-sided")
print(thesap,p)

if p<alpha:
    print("H0 Denied")
else:
    print("H0 Not Denied")

#H0 Denied. Students from 2 different schools have different average scores on the test.