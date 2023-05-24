## This file is to run sample trial cases before adding to the main files

import pandas as pd

df1 = pd.DataFrame({'userID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    'a2': ['A', 'A', 'A', 'B', 'B', 'B', 'A', 'A',  'A', 'C'],
                    'a1': [2015, 2015, 2015, 2016, 2016, 2016, 2016, 2016, 2016, 2017],
                    'a3': ['aa', 'bb', 'cc', 'aa', 'aa', 'cc', 'cc', 'cc',  'cc', 'cc'],
                    'a4': [33, 33, 37, 38, 33, 39, 34, 34,  35, 35]})

#print(df1['a1'])
serr = df1['a1']
arr = serr.to_list()
#arr = arr.sort()
print(serr)
#o2 = serr[1]
#print(o2)
print(arr)
ind = serr[serr == arr[1]]
print(ind)

# Get the index series when the data is sorted in descending order
descending_indexes = serr.argsort()[::-1]

# Convert the index series to a list
descending_indexes_list = descending_indexes.tolist()

print(descending_indexes_list)





