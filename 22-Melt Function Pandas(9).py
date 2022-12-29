import pandas as pd


data=pd.read_excel("C:/Users/MSTF/Desktop/Basic Statistic/9.xlsx")
data2=data.copy()

data3=pd.melt(data2,id_vars=["Position"],value_vars=["1 Month","5 Months","1 Year","3+ Years"])
data3.columns=["Position","Duration","Performance"]
print(data3)