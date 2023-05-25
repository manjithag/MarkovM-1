## This file is to run sample trial cases before adding to the main files

import pandas as pd
from itertools import permutations

df1 = pd.DataFrame({'userID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    'a2': ['A', 'A', 'A', 'B', 'B', 'B', 'A', 'A',  'A', 'C'],
                    'a1': [2015, 2015, 2015, 2016, 2016, 2016, 2016, 2016, 2016, 2017],
                    'a3': ['aa', 'bb', 'cc', 'aa', 'aa', 'cc', 'cc', 'cc',  'cc', 'cc'],
                    'a4': [33, 33, 37, 38, 33, 39, 34, 34,  35, 35]})

#print(df1['a1'])
serr = df1['a1']
arr = serr.to_list()
#arr = arr.sort()
#print(serr)
#o2 = serr[1]
#print(o2)
#print(arr)
ind = serr[serr == arr[1]]
#print(ind)

# Get the index series when the data is sorted in descending order
descending_indexes = serr.argsort()[::-1]

# Convert the index series to a list
descending_indexes_list = descending_indexes.tolist()

#print(descending_indexes_list)




sample_list = ['a', 'b', 'c']

def find_attri_combinations(attributes):

    # The function find only the combinations with all elements. (Equal to the length of the attributes list)
    length_combinations = len(attributes)

    # Generate all the shuffled combinations of the elements (With all elements) of the attribute list
    all_combinations = list(permutations(attributes, length_combinations))

    # A list for storing the combinations excluding symmetric
    combinations_without_symm = []

    # Checking for the list with its reversed lists
    for comb in all_combinations:
        if comb not in combinations_without_symm and comb[::-1] not in combinations_without_symm:
            combinations_without_symm.append(comb)

    return combinations_without_symm

#print(find_attri_combinations(sample_list))



#print(list_combinations)



arr = ['a', 'b', 'c']
char = 'd'
#print(arr+list(char))

arr = [0.2, 1, 5, 0]
#print(arr)
arr.sort(reverse=True)
#print(arr)



arr = ['a1', 'a2', 'a4', 'a3']
data = ['a1', 'a2']
char = 'a5'

arr.remove(char)
print(arr)








