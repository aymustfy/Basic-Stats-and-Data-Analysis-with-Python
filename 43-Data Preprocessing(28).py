import pandas as pd

### Kaggle link for dataset ----> https://www.kaggle.com/datasets/mathchi/online-retail-ii-data-set-from-ml-repository

#data=pd.read_excel("C:/Users/MSTF/Desktop/Basic Statistic/28.xlsx")
#data.to_csv("C:/Users/MSTF/Desktop/Basic Statistic/28.csv")

data=pd.read_csv("C:/Users/MSTF/Desktop/Basic Statistic/28.csv")
data2=data.copy()

data2.drop(data2.columns[[0]],axis=1,inplace=True)

data2["TotalAmount"]=data2["Price"]*data2["Quantity"]
data2["InvoiceDate"]=pd.to_datetime(data2["InvoiceDate"])

data2.drop("Customer ID",axis=1,inplace=True)

data2.dropna(axis=0,inplace=True)
data2.reset_index(drop=True,inplace=True)
###############
cancellation=data2[data2["Invoice"].str.contains("C",na=False)]
cancellationindex=[]

for i in cancellation.index:
    cancellationindex.append(i)

data2.drop(data2.index[cancellationindex],inplace=True)
data2.reset_index(drop=True,inplace=True)
###############
error=data2[(data2["Invoice"].str.len()!=6) | (~data2["Invoice"].str.isdigit())]
errorindex=[]

for i in error.index:
    errorindex.append(i)

data2.drop(data2.index[errorindex],inplace=True)
data2.reset_index(drop=True,inplace=True)
###############
error2=data2[(data2["StockCode"].str.len()!=5) | (~data2["StockCode"].str.isdigit())]
error3=data2[~data2["StockCode"].str.isdigit()]

errorindex2=[]
for i in error3.index:
    errorindex2.append(i)

data2.drop(data2.index[errorindex2],inplace=True)
data2.reset_index(drop=True,inplace=True)
###############
error4=data2[data2["Quantity"]<=0]
errorindex3=[]
for i in error4.index:
    errorindex3.append(i)

data2.drop(data2.index[errorindex3],inplace=True)
data2.reset_index(drop=True,inplace=True)
###############
error5=data2[data2["Price"]<=0]
errorindex4=[]
for i in error5.index:
    errorindex4.append(i)

data2.drop(data2.index[errorindex4],inplace=True)
data2.reset_index(drop=True,inplace=True)
###############
for j in ["Quantity","Price","TotalAmount"]:
    q1=data2[j].quantile(0.25)
    q3=data2[j].quantile(0.75)
    IQR=q3-q1

    upperlimit=q3+1.5*IQR
    lowerlimit=q3-1.5*IQR

    outlier=data2[(data2[j]>upperlimit) | (data2[j]<lowerlimit)]
errorindex5=[]
for i in outlier.index:
    errorindex5.append(i)
data2.drop(data2.index[errorindex5],inplace=True)
data2.reset_index(drop=True,inplace=True)

data2=pd.get_dummies(data=data2,columns=["Country"],drop_first=True)

print(data2)
