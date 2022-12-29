import pandas as pd
from sklearn import preprocessing as pr

data=pd.read_excel("C:/Users/MSTF/Desktop/Basic Statistic/26.xlsx")
data2=data.copy()

#Scales data from 0 to 1
MaxMinTransform=pr.MinMaxScaler().fit_transform(data2)
data3=pd.DataFrame(MaxMinTransform)
print(data3)

#Similar to normalization but positive for too many outliers
RebostTransform=pr.RobustScaler().fit_transform(data2)
data4=pd.DataFrame(RebostTransform)
print(data4)

#It sets the mean value to 0, sets the standard deviation to 1, and brings the distribution closer to normal.
StdScaleTransform=pr.StandardScaler().fit_transform(data2)
data5=pd.DataFrame(StdScaleTransform)
print(data5)
