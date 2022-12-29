import seaborn as sns
from sklearn import preprocessing as pr

data=sns.load_dataset("tips")
data2=data.copy()
print(data2)

data2["DayCode"]=pr.LabelEncoder().fit_transform(data2["day"])
print(data2)
#In this example, the days are encoded as numeric values between 0 and 6, doing some sort of scaling.

#However, this digital transformation can cause problems in machine learning algorithms.

#Different problems arise in the case of hierarchical structures in the categorical variable structure or not. In the case of hierarchical structures, the program does the numbering differently.

#For example, for the education level, there should be a hierarchical cycle such as primary school = 0, high school = 1, university = 2, graduate = 3, while the program assigns these hierarchical numbers randomly. 
# We will see the solution to this problem in the future.

#In variables such as gender and color, where there is no hierarchical structure, the algorithm perceives hierarchical structures, although there is no categorical structure. 
# To prevent this, one-hot encoding is done on these variables.

