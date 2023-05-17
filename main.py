import pandas as pd

df = pd.DataFrame({'recID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    'a1': [2015, 2015, 2015, 2016, 2016, 2016, 2016, 2016, 2016, 2017],
                    'a2': ['A', 'A', 'A', 'B', 'B', 'B', 'A', 'A',  'A', 'C']})

def calc_StartProbability(attri,var):

    # Calculate the start probability of a given attribute and its value
    no_records = df.shape[0]      #Calculating the number of records
    occurence = df[attri].value_counts()[var] # Calculating the number of occurences of the specific value

    return occurence/no_records # Returning start probability

def calc_ObservationProbability():
    pass



def calc_MMRisk(recID,attr):
    pass







print(calc_StartProbability('a1',2015))
print(calc_StartProbability('a1',2016))
print(calc_StartProbability('a1',2017))




