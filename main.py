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
    df2 = df.loc[df['userID'] == 2]
    var = df2.loc[:, attri]         # Obtaining the value of the given attribute and given userID
    print(var)
    occurence = df[attri].value_counts()[var]  # Calculating the number of occurences of the specific value

    return (1-1/occurence)








def calc_MMRisk(userID,attr):
    pass







#print(calc_StartProbability('a1',2015))
#print(calc_StartProbability('a1',2016))
#print(calc_StartProbability('a1',2017))

#print(calc_ObservationProbability(1,'a1'))
#print(calc_ObservationProbability(2,'a1'))

df2 = df.loc[df['userID'] == 3]
df3 = df2['a1']
print(df3)