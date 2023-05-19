## MM Risk Calculation with duplicates of users ##

import pandas as pd

df = pd.DataFrame({'userID': [1, 1, 1, 4, 5, 6, 7, 8, 9, 10],
                    'a1': [2015, 2015, 2015, 2016, 2016, 2016, 2016, 2016, 2016, 2017],
                    'a2': ['A', 'A', 'A', 'B', 'B', 'B', 'A', 'A',  'A', 'C']})

sensitive_attri = ['a1','a2']

def calc_StartProbability(index,attri):
    # Calculate the start probability of a given attribute and index

    no_records = df.shape[0]        # Counting the number of records of the dataset
    val = df.loc[index][attri]      # Obtaining the value of the given attribute for the given index
    occurrence = df[attri].value_counts()[val]      # Calculating the number of occurrences of the specific value

    return occurrence/no_records           # Returning start probability

def calc_ObservationProbability(index,attri):

    attri_val = df.loc[index][attri]
    userID  = df.loc[index]['userID']

    df2 = df.loc[df[attri] == attri_val]
    no_records = df2.shape[0]            # Counting the number of records of the dataset
    val = df2.loc[index, attri]         # Obtaining the value of the given attribute and given userID

    occurrence = df2['userID'].value_counts()[userID]  # Calculating the number of occurences of the specific value

    return (1-occurrence/no_records)

def calc_TransitionProbability(userID):
    # Calculates P(vj+1/vj )

    index = userID - 1  # This is not always right. TO DO : Do the changes when the same userID repeats
    val1 = df.loc[index]['a1']
    val2 = df.loc[index]['a2']

    occurrence_attri1 = df['a1'].value_counts()[val1]  # Calculating the number of occurrences of the specific value

    df3 = df.loc[df['a1'] == val1]
    occurrence_attri2 = df3['a2'].value_counts()[val2]  # Calculating the number of occurrences of the specific value

    return occurrence_attri2/occurrence_attri1

def calc_MMRisk(userID,attri):
    attri1 = attri          # Assigning the passed attribute

    for i in sensitive_attri:      # Assigning the other attribute
        if attri1 != i:
          attri2 = i

    MMProb = calc_StartProbability(userID,attri1)*calc_ObservationProbability(userID,attri1)*calc_TransitionProbability(userID)*calc_ObservationProbability(userID,attri2)
    MMRisk = 1 - MMProb

    MMRisk = round(MMRisk,3)        # Round off the value of MMRisk to 3 decimal points

    return MMRisk


########  TEST ########


for i in range (10):        # Looping by index of the dataset
    #print(calc_StartProbability(i,'a1'))
    print(calc_ObservationProbability(i, 'a1'))
    #print(calc_ObservationProbability(i, 'a2'))
    #print(calc_TransitionProbability(i))



"""
for i in range (1,11):
    print(calc_MMRisk(i,'a1'))

print('\n')

for i in range (1,11):
    print(calc_MMRisk(i,'a2'))

"""
