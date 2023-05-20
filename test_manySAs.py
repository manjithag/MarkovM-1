import pandas as pd
from mmRisk_manySAs import create_Risk_Dataframe

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
                    'a2': ['A', 'A', 'A', 'B', 'B', 'B', 'A', 'A',  'A', 'C'],
                    'a3': [33, 33, 37, 38, 33, 39, 34, 34,  35, 35]})

## Test Case 5 : 4 nos sensitive attributes without duplicates of users
df5 = pd.DataFrame({'userID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    'a1': [2015, 2015, 2015, 2016, 2016, 2016, 2016, 2016, 2016, 2017],
                    'a2': ['A', 'A', 'A', 'B', 'B', 'B', 'A', 'A',  'A', 'C'],
                    'a3': [33, 33, 37, 38, 33, 39, 34, 34,  35, 35],
                    'a4': ['aa', 'bb', 'cc', 'aa', 'aa', 'cc', 'cc', 'cc',  'cc', 'cc'],})

## Test Case 6 : 4 nos sensitive attributes without duplicates of users
df6 = pd.DataFrame({'userID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    'a2': ['A', 'A', 'A', 'B', 'B', 'B', 'A', 'A',  'A', 'C'],
                    'a1': [2015, 2015, 2015, 2016, 2016, 2016, 2016, 2016, 2016, 2017],
                    'a3': ['aa', 'bb', 'cc', 'aa', 'aa', 'cc', 'cc', 'cc',  'cc', 'cc'],
                    'a4': [33, 33, 37, 38, 33, 39, 34, 34,  35, 35]})

sensitive_attri1 = ['a1','a2']    # Valid for all test cases (Shortly known as SA)
sensitive_attri2 = ['a1','a2','a3']    # Valid for test case 4 (Shortly known as SA)
sensitive_attri3 = ['a2','a1','a3']    # Valid for test case 4 (Shortly known as SA)
sensitive_attri4 = ['a2','a3','a1']    # Valid for test case 4 (Shortly known as SA)
sensitive_attri5 = ['a2','a1']

sensitive_attri6 = ['a1','a2','a3','a4']    # Valid for test case 5 (Shortly known as SA)
sensitive_attri7 = ['a2','a4','a3','a1']    # Valid for test case 5 (Shortly known as SA)
sensitive_attri8 = ['a2','a4','a1','a3']    # Valid for test case 5 (Shortly known as SA)

########  TEST ########

#print(create_Risk_Dataframe(df1,sensitive_attri1))
#print(create_Risk_Dataframe(df2,sensitive_attri))
#print(create_Risk_Dataframe(df3,sensitive_attri))
#print(create_Risk_Dataframe(df4,sensitive_attri2))

#create_Risk_Dataframe(df4,sensitive_attri2)
#create_Risk_Dataframe(df4,sensitive_attri3)
#create_Risk_Dataframe(df4,sensitive_attri4)

#create_Risk_Dataframe(df3,sensitive_attri1)
#create_Risk_Dataframe(df3,sensitive_attri5)

create_Risk_Dataframe(df5,sensitive_attri6)
create_Risk_Dataframe(df5,sensitive_attri7)
create_Risk_Dataframe(df6,sensitive_attri6)