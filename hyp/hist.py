#histogram program for Tips project by RSS
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import sys

tips = [20.8, 18.7, 19.1, 20.6, 21.9, 20.4, 22.8,
21.9, 21.2, 20.3, 21.9, 18.3, 21.0, 20.3,
19.2, 20.2, 21.1, 22.1, 21.0, 21.7]

plt.hist(tips,5,normed=True)
plt.title("Sample Tips After Free Beer")
plt.xlabel("Tip %")
plt.ylabel("Density")
plt.text(18.5,.23,"Sample mean = 20.73")
plt.show()
