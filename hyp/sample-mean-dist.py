#histogram program for Tips project by RSS
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import math
import sys

tips = [20.8, 18.7, 19.1, 20.6, 21.9, 20.4, 22.8,
21.9, 21.2, 20.3, 21.9, 18.3, 21.0, 20.3,
19.2, 20.2, 21.1, 22.1, 21.0, 21.7]

mean=np.mean(tips)
stddev=np.std(tips)

x=np.arange(18,22,.001)
plt.axis([18.0,22.0,0,1.6])
y=stats.norm.pdf(x,20.0,((stddev)/math.sqrt(len(tips))))
plt.plot(x,y,color='red')
plt.title("Tips control ($H_{0}$) sample mean density")
plt.xlabel("Average Tip %")
plt.ylabel("Density")
plt.text(18.5,.23,"Sample mean = 20.73")
plt.plot(20.73,0,"d")
plt.show()