import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt

data=pd.read_excel("C:/Users/MSTF/Desktop/Basic Statistic/23.xlsx")
data2=data.copy()

### Missing Value Detect
print(data2.info())
print(data2.isnull())

print(data2[data2.isnull().any(axis=1)])

msno.bar(data2)
plt.show()
msno.matrix(data2)
plt.show()


### Randomness Check
data3=data2.notnull().astype("int")
print(data3.corr())

# Full data is assigned 1 and empty data is assigned 0. Afterwards, a correlation test is performed. 
# If the correlation coefficient between the variables is below 0.8, it can be said that missing values occur randomly.