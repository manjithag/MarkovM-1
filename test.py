import pandas as pd
from with_duplicates import create_Result_Dataset


## Test Case 1 : Without duplicates of users
df1 = pd.DataFrame({'userID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    'a1': [2015, 2015, 2015, 2016, 2016, 2016, 2016, 2016, 2016, 2017],
                    'a2': ['A', 'A', 'A', 'B', 'B', 'B', 'A', 'A',  'A', 'C']})

## Test Case 2 : With duplicates of users
df2 = pd.DataFrame({'userID': [1, 1, 1, 4, 5, 6, 7, 8, 9, 10],
                    'a1': [2015, 2015, 2015, 2016, 2016, 2016, 2016, 2016, 2016, 2017],
                    'a2': ['A', 'A', 'A', 'B', 'B', 'B', 'A', 'A',  'A', 'C']})

## Test Case 3 : With duplicates of users containing different attribute values
df3 = pd.DataFrame({'userID': [1, 2, 3, 4, 5, 6, 1, 1, 7, 8],
                    'a1': [2015, 2015, 2015, 2016, 2016, 2016, 2016, 2016, 2016, 2017],
                    'a2': ['A', 'A', 'A', 'B', 'B', 'B', 'A', 'A',  'A', 'C']})

sensitive_attri = ['a1','a2']    # Valid for all test cases
attri = 'a1'

########  TEST ########

create_Result_Dataset(df1,sensitive_attri)
#create_Result_Dataset(df2,sensitive_attri)
#create_Result_Dataset(df3,sensitive_attri)



