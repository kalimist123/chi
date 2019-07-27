
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


'''
The NumPy package has a random module that has a normal function, where 50 is
given as the mean of the distribution, 10 is the standard deviation of the distribution,
and 60 is the number of values to be generated
'''


classscore = np.random.normal(50, 10, 60).round()
print(classscore)

plt.hist(classscore, 30, density=True)
plt.show()

zscore = ( 68 - classscore.mean() ) / classscore.std()
print('zscore:', zscore)

'''
The cdf function gives the probability of getting values up to the z-score,
and doing a minus one of it will give us the probability of getting a z-score, which
is above it. In other words, 0.09 is the probability of getting marks above 60.
'''

prob = 1 - stats.norm.cdf(zscore)
print('pscore:',prob)

