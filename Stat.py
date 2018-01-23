from scipy import *
from pylab import *
import sys
import matplotlib.pyplot as plt
import numpy as np

import statsmodels.formula.api as smf
import statsmodels.tsa.api as smt
import statsmodels.api as sm

N = 1000;
mu = 0;
sigma = 1;

#X = np.random.normal(mu, sigma, N);
#print(X)

#plt.plot(X)
#plt.ylabel('normal random variables')
#plt.show()

X = np.ones(N)
a1 = 0.8;
a2 = 0.9;
e = np.random.normal(mu, sigma, N)

for i in range(2,N):
    X = a1*X + e

plt.plot(X)
plt.xlabel('Simulated AR(1)-process')
plt.show()





