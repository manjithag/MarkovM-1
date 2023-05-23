#load necessary packages and functions
import scipy.stats as stats
import numpy as np
import pandas as pd

df = pd.DataFrame({'userID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    'a1': [2015, 2015, 2015, 2016, 2016, 2016, 2016, 2016, 2016, 2017],
                    'a2': ['A', 'A', 'A', 'B', 'B', 'B', 'A', 'A',  'A', 'C'],
                    'a3': [33, 33, 37, 38, 33, 39, 34, 34,  35, 35],
                    'a4': ['aa', 'bb', 'cc', 'aa', 'aa', 'cc', 'cc', 'cc',  'cc', 'cc'],})


data1 = pd.crosstab(df['a1'], df['a2'])

#create 2x2 table
data = np.array([[6,9], [8, 5], [12, 9]])

#Chi-squared test statistic, sample size, and minimum of rows and columns
X2 = stats.chi2_contingency(data, correction=False)[0]
n = np.sum(data)
minDim = min(data.shape)-1

#calculate Cramer's V
V = np.sqrt((X2/n) / minDim)

#display Cramer's V
print(V)
print(data1)
print(X2)



