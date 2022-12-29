import pandas as pd
from sklearn import preprocessing as pr
from sklearn.preprocessing import LabelEncoder
import numpy as np

data=pd.read_excel("C:/Users/MSTF/Desktop/Basic Statistic/27.xlsx")
data2=data.copy()

#Categorical variables created
data2["CodGender"]=pr.LabelEncoder().fit_transform(data2["Gender"])
data2["CodCarColor"]=pr.LabelEncoder().fit_transform(data2["CarColor"])


onehotencoding=pd.get_dummies(data2,columns=["Gender","CarColor"],drop_first=True)
#Drop_first applied for escape from dummy variable trap

#Hiearchical variable identified
hierarchy=pd.Categorical(data2["Education"],categories=["Primary School","High School","University","Master","PhD"],ordered=True)

data2["Hierarchical Education"],ordinal=pd.factorize(hierarchy,sort=True)
print(data2)


