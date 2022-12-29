import pandas as pd

data=pd.read_excel("C:/Users/MSTF/Desktop/Basic Statistic/23.xlsx")
data2=data.copy()

data2.dropna(inplace=True)
data2.reset_index(drop=True,inplace=True)
print(data2)
#----> delete all rows except rows that are completely filled

data2.dropna(inplace=True, how="all")   
#----> delete rows if all values missing in row 

data2.fillna(value="Missing Values",inplace=True)
# Fill missing values in column as "Missing Values".

data2["D1"].fillna(value=data2["D1"].mean(),inplace=True)
# Fill missing values in column mean values.

data2.fillna(value=data2.mean()["D1":"D2"],inplace=True)
# Fill all missing values in columns(D1,D2) mean values.

data2.fillna(value=data2.mean()[:],inplace=True)
# Fill in all missing values in the columns with the average values of that column.


data3=pd.read_excel("C:/Users/MSTF/Desktop/Basic Statistic/24.xlsx")
data4=data3.copy()

data4["Age"].fillna(data4.groupby("Gender")["Age"].transform("mean"),inplace=True)
print(data4)
#Each missing value in the column was filled with the mean values of that gender.

data5=pd.read_excel("C:/Users/MSTF/Desktop/Basic Statistic/25.xlsx")
data6=data5.copy()

data6["City"].fillna(data6["City"].mode()[0],inplace=True)
print(data6)
#The missing value in the column was filled with the name of the city with the most counts(Mode).
