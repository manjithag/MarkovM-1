## This test the workflow.py

import pandas as pd
from workflow import find_workflow

## Test Case 1 : 4 nos attributes
df1 = pd.DataFrame({'userID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    'a2': ['A', 'A', 'A', 'B', 'B', 'B', 'A', 'A',  'A', 'C'],
                    'a1': [2015, 2015, 2015, 2016, 2016, 2016, 2016, 2016, 2016, 2017],
                    'a3': ['aa', 'bb', 'cc', 'aa', 'aa', 'cc', 'cc', 'cc',  'cc', 'cc'],
                    'a4': [33, 33, 37, 38, 33, 39, 34, 34,  35, 35]})

attributes1 = ['a1','a2','a3','a4']
attributes2 = ['a3','a1','a4','a2']

print(find_workflow(df1,attributes1,0.5))
#find_workflow(df1,attributes2)



