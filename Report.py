
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.tsa.api as smt
import statsmodels.api as sm


N = 1000
x = w = np.random.normal(size=N)
for i in range(N):
    x[i] = x[i-1] + w[i]

data = x
f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
plot_1 = smt.graphics.plot_acf(data, lags=30, ax=ax1)
plot_2 = smt.graphics.plot_pacf(data, lags=30, ax=ax2)
ax3.plot(data)
plot_4 = sm.qqplot(data, line='s', ax=ax4)
plt.style.use('dark_background')
plt.show()

