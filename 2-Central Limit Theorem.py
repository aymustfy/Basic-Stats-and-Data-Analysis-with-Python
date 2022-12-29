import numpy as np
import matplotlib.pyplot as plt
import random

age=np.random.uniform(low=18,high=75,size=40000)

sample=[np.mean(random.choices(age,k=30))for _ in range(1000)]

plt.hist(sample)
plt.show()