## MM Risk Calculation without duplicates of users ##

import pandas as pd

df = pd.DataFrame({'userID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    'a1': [2015, 2015, 2015, 2016, 2016, 2016, 2016, 2016, 2016, 2017],
                    'a2': ['A', 'A', 'A', 'B', 'B', 'B', 'A', 'A',  'A', 'C']})

sensitive_attri = ['a1','a2']

def calc_StartProbability(userID,attri):

    # Calculate the start probability of a given attribute and UserID

    index = userID - 1  # This is not always right. TO DO : Do the changes when the same userID repeats
    val = df.loc[index][attri]
    no_records = df.shape[0]      #Calculating the number of records of the dataset
    occurence = df[attri].value_counts()[val] # Calculating the number of occurences of the specific value

    return occurence/no_records # Returning start probability

def calc_ObservationProbability(userID,attri):
    df2 = df.loc[df['userID'] == userID]
    index = userID-1       # This is not always right. TO DO : Do the changes when the same userID repeats
    val = df2.loc[index, attri]         # Obtaining the value of the given attribute and given userID
    #print(var)
    occurence = df[attri].value_counts()[val]  # Calculating the number of occurences of the specific value

    return (1-1/occurence)

def calc_TransitionProbability(userID):
    # Calculates P(vj+1/vj )

    index = userID - 1  # This is not always right. TO DO : Do the changes when the same userID repeats
    val1 = df.loc[index]['a1']
    val2 = df.loc[index]['a2']

    occurence_attri1 = df['a1'].value_counts()[val1]  # Calculating the number of occurences of the specific value
    #print(occurence_attri1)

    df3 = df.loc[df['a1'] == val1]
    occurence_attri2 = df3['a2'].value_counts()[val2]  # Calculating the number of occurences of the specific value
    #print(df3)
    #print(occurence_attri2)

    return occurence_attri2/occurence_attri1




def calc_MMRisk(userID,attri):

    attri1 = attri

    for i in sensitive_attri:
        if attri1 != i:
          attri2 = i

    MMProb = calc_StartProbability(userID,attri1)*calc_ObservationProbability(userID,attri1)*calc_TransitionProbability(userID)*calc_ObservationProbability(userID,attri2)
    MMRisk = 1 - MMProb

    MMRisk = round(MMRisk,3)        # Round off the value of MMRisk to 3 decimal points

    return MMRisk


########  TEST ########

#print(calc_StartProbability('a1',2015))
#print(calc_StartProbability('a1',2016))
#print(calc_StartProbability('a1',2017))

#print(calc_ObservationProbability(1,'a1'))
#print(calc_ObservationProbability(4,'a1'))
#print(calc_ObservationProbability(10,'a1'))

"""
for i in range (1,11):
    print(calc_StartProbability(i,'a1'))
    #print(calc_ObservationProbability(i, 'a1'))
    #print(calc_ObservationProbability(i, 'a2'))
    #print(calc_TransitionProbability(i))

"""
for i in range (1,11):
    print(calc_MMRisk(i,'a1'))

print('\n')

for i in range (1,11):
    print(calc_MMRisk(i,'a2'))


