import pandas as pd
from with_duplicates import calc_MMRisk,calc_StartProbability,calc_ObservationProbability,calc_TransitionProbability

df = pd.DataFrame({'userID': [1, 1, 1, 4, 5, 6, 7, 8, 9, 10],
                    'a1': [2015, 2015, 2015, 2016, 2016, 2016, 2016, 2016, 2016, 2017],
                    'a2': ['A', 'A', 'A', 'B', 'B', 'B', 'A', 'A',  'A', 'C']})

sensitive_attri = ['a1','a2']

########  TEST ########

'''
for i in range (10):        # Looping by index of the dataset
    #print(calc_StartProbability(i,'a1'))
    #print(calc_ObservationProbability(i, 'a1'))
    #print(calc_ObservationProbability(i, 'a2'))
    #print(calc_TransitionProbability(i,'a1'))

'''


for i in range (10):
    print(calc_MMRisk(i,'a1'))

print('\n')

for i in range (10):
    print(calc_MMRisk(i,'a2'))



