import numpy as np
import matplotlib.pyplot as plt


age=np.random.normal(loc=40,scale=5,size=40000)

plt.figure()
plt.title("Age Frequency")
plt.xlabel("Age")
plt.ylabel("Frequence")
plt.hist(age,color="b",histtype="bar",bins=35)
plt.show()
