import pandas as pd

df = pd.DataFrame({'userID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    'a1': [2015, 2015, 2015, 2016, 2016, 2016, 2016, 2016, 2016, 2017],
                    'a2': ['A', 'A', 'A', 'B', 'B', 'B', 'A', 'A',  'A', 'C']})

def calc_StartProbability(attri,var):

    # Calculate the start probability of a given attribute and its value
    no_records = df.shape[0]      #Calculating the number of records
    occurence = df[attri].value_counts()[var] # Calculating the number of occurences of the specific value

    return occurence/no_records # Returning start probability

def calc_ObservationProbability(userID,attri):
    df2 = df.loc[df['userID'] == userID]
    index = userID-1       # This is not always right. TO DO : Do the changes when the same userID repeats
    var = df2.loc[index, attri]         # Obtaining the value of the given attribute and given userID
    #print(var)
    occurence = df[attri].value_counts()[var]  # Calculating the number of occurences of the specific value

    return (1-1/occurence)

def calc_TransitionProbability(userID):
    # Calculates P(vj+1/vj )

    index = userID - 1  # This is not always right. TO DO : Do the changes when the same userID repeats
    attri1 = df.loc[[index,'a1']]
    attri2 = df.loc[[index, 'a2']]

    print(attri2)
    print(' & ')
    print(attri1)





def calc_MMRisk(userID,attr):
    pass







#print(calc_StartProbability('a1',2015))
#print(calc_StartProbability('a1',2016))
#print(calc_StartProbability('a1',2017))

#print(calc_ObservationProbability(1,'a1'))
#print(calc_ObservationProbability(4,'a1'))
#print(calc_ObservationProbability(10,'a1'))

print(calc_TransitionProbability(1))
#print(calc_TransitionProbability(4))
#print(calc_TransitionProbability(10))