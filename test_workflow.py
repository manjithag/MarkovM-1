## This test the workflow.py

import pandas as pd
from workflow import find_workflow

## Test Case 1 : 4 nos attributes
df1 = pd.DataFrame({'userID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    'a2': ['A', 'A', 'A', 'B', 'B', 'B', 'A', 'A',  'A', 'C'],
                    'a1': [2015, 2016, 2017, 2017, 2016, 2015, 2016, 2016, 2016, 2017],
                    'a3': ['aa', 'bb', 'aa', 'aa', 'aa', 'cc', 'cc', 'cc',  'cc', 'cc'],
                    'a4': [33, 33, 37, 38, 33, 39, 34, 34,  35, 35]})

## Test Case 2 : 4 nos attributes
df2 = pd.DataFrame({'userID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    'a1': [2015, 2015, 2015, 2016, 2016, 2016, 2016, 2016, 2016, 2017],
                    'a2': ['A', 'A', 'A', 'B', 'B', 'B', 'A', 'A',  'A', 'C'],
                    'a3': [33, 33, 37, 38, 33, 39, 34, 34,  35, 35],
                    'a4': ['aa', 'bb', 'cc', 'aa', 'aa', 'cc', 'cc', 'cc',  'cc', 'cc'],})

attributes1 = ['a1','a2','a3','a4']


#print(find_workflow(df1,attributes1,0.999))
print(find_workflow(df2,attributes1,0.999))




