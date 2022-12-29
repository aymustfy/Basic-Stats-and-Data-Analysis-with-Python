import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

np.random.seed(0)
data=np.random.normal(35,2,4000)
data2=data.copy()

zScore=stats.zscore(data2)

sns.displot(zScore,kde=True)
plt.title("ZScore Histogram", fontsize=15,loc="right",c="red")
plt.xlabel("Age", fontsize=15,c="red")
plt.ylabel("Freq",fontsize=15,c="red")

plt.xlim(-3,3)
plt.axvline(x=np.mean(zScore),linestyle="--",linewidth=2.5,label="Mean",c="red")
plt.axvline(x=np.mean(zScore)-np.std(zScore),linestyle="--",linewidth=2.5,label="1 Std",c="green")
plt.axvline(x=np.mean(zScore)+np.std(zScore),linestyle="--",linewidth=2.5,label="1 Std",c="green")
plt.axvline(x=np.mean(zScore)-2*np.std(zScore),linestyle="--",linewidth=2.5,label="2 Std",c="blue")
plt.axvline(x=np.mean(zScore)+2*np.std(zScore),linestyle="--",linewidth=2.5,label="2 Std",c="blue")
plt.axvline(x=np.mean(zScore)-3*np.std(zScore),linestyle="--",linewidth=2.5,label="3 Std",c="red")
plt.axvline(x=np.mean(zScore)+3*np.std(zScore),linestyle="--",linewidth=2.5,label="3 Std",c="red")

plt.legend()
plt.show()

