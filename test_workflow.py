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

## Test Case 3 : 5 nos attributes
df3 = pd.DataFrame({'userID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    'a1': [2015, 2015, 2015, 2016, 2016, 2016, 2016, 2016, 2016, 2017],
                    'a2': ['A', 'A', 'A', 'B', 'B', 'B', 'A', 'A',  'A', 'C'],
                    'a3': [33, 33, 37, 38, 33, 39, 34, 34,  35, 35],
                    'a4': ['aa', 'bb', 'cc', 'aa', 'aa', 'cc', 'cc', 'cc',  'cc', 'cc'],
                    'a5': [123, 121, 125, 125, 121, 127, 123, 127, 121, 128],})

## Test Case 4 : 6 nos attributes
df4 = pd.DataFrame({'userID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    'a1': [2015, 2015, 2015, 2016, 2016, 2016, 2016, 2016, 2016, 2017],
                    'a2': ['A', 'A', 'A', 'B', 'B', 'B', 'A', 'A',  'A', 'C'],
                    'a3': [33, 33, 33, 33, 33, 33, 34, 33,  35, 35],
                    'a4': ['aa', 'bb', 'cc', 'aa', 'aa', 'cc', 'cc', 'cc',  'cc', 'cc'],
                    'a5': [123, 121, 125, 125, 121, 127, 123, 127, 121, 128],
                    'a6': [5, 8, 5, 9, 6, 4, 4, 9, 9, 9] })

## Test Case 5 : Import csv file : 5 nos attributes
df5 = pd.read_csv('OULA student assessment.csv')

attributes1 = ['a1','a2','a3','a4']
attributes2 = ['a1','a2','a3','a4','a5']
attributes3 = ['a1','a2','a3','a4','a5', 'a6']
attributes4 = list(df5.columns)

#### Running Tests

#print(find_workflow(df1,attributes1,0.999))
#print(find_workflow(df2,attributes1,0.999))
#print(find_workflow(df3,attributes2,0.99999))
print(find_workflow(df4,attributes3,0.99))
#print(find_workflow(df5,attributes4,0.99))


