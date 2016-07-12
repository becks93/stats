#t-test program for Tips project by RSS
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import math
import sys

tips = [20.8, 18.7, 19.1, 20.6, 21.9, 20.4, 22.8,
21.9, 21.2, 20.3, 21.9, 18.3, 21.0, 20.3,
19.2, 20.2, 21.1, 22.1, 21.0, 21.7]

N=len(tips)
mean=np.mean(tips)
stddev=np.std(tips,ddof=1)

t=(mean-20)/(stddev/math.sqrt(N))

oneside_pval=1-stats.t.cdf(t,N-1)
twoside_pval=2*oneside_pval
print "t is ",t
print "one-sided p-value is ", oneside_pval
print "two-sided p-value is ", twoside_pval
print"p-value (from t-test) = ",twoside_pval, ", Reject H0"