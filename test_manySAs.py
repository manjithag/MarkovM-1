import pandas as pd
from mmRisk_2SA import create_Risk_Dataframe

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

## Test Case 4 : 3 nos sensitive attributes without duplicates of users
df4 = pd.DataFrame({'userID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    'a1': [2015, 2015, 2015, 2016, 2016, 2016, 2016, 2016, 2016, 2017],
                    'a2': ['A', 'A', 'A', 'B', 'B', 'B', 'A', 'A',  'A', 'C']
                    'a3': [33, 33, 37, 38, 33, 39, 34, 34,  35, 35]})


sensitive_attri = ['a1','a2','a3']    # Valid for all test cases (Shortly known as SA)

########  TEST ########

#print(create_Risk_Dataframe(df1,sensitive_attri))
#print(create_Risk_Dataframe(df2,sensitive_attri))
#print(create_Risk_Dataframe(df3,sensitive_attri))
print(create_Risk_Dataframe(df4,sensitive_attri))