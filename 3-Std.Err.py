import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x=np.random.normal(35,1,10000)
sns.displot(x,kde=True)
plt.show()

