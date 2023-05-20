## MM Risk Calculation with and without duplicates of users
## Valid for many (more than 2) sensitive attributes

import pandas as pd
def create_Risk_Dataframe(df:pd.DataFrame,sensitive_attri:list):

    """
    Returns a dataframe with the values of risk of re-identification for each record (users / index)
    and for each sensitive attributes

        INPUTS  : df = Original dataset : Pandas dataframe
                  sensitive_attri = Column names of sensitive attributes : List

        RETURN  : Risks of re-identifications dataset : Pandas dataframe
    """


    def calc_StartProbability(index,attri):
        # Calculate the start probability of a given attribute and index --> P(attri = attri_val)

        no_records = df.shape[0]        # Counting the number of records of the dataset
        attri_val = df.loc[index][attri]      # Obtaining the value of the given attribute for the given index
        occurrence = df[attri].value_counts()[attri_val]      # Calculating the number of occurrences of the specific value

        return occurrence/no_records           # Returning start probability

    def calc_ObservationProbability(index,attri):
        # Calculate the observation probability of a given attribute and index
        # --> 1 - P(user = attri_val / attri = attri_val)

        attri_val = df.loc[index][attri]
        userID  = df.loc[index]['userID']

        df2 = df.loc[df[attri] == attri_val]
        no_records = df2.shape[0]            # Counting the number of records of the dataset

        occurrence = df2['userID'].value_counts()[userID]  # Calculating the number of occurences of the specific value

        return (1-occurrence/no_records)

    def calc_TransitionProbability(index,attri1,attri2):
        # Calculates the transition probability from given attribute to next attribute
        # --> P(attri2 = attri2_val / attri1 = attri1_val)

        val_attri1 = df.loc[index][attri1]
        val_attri2 = df.loc[index][attri2]

        df3 = df.loc[df[attri1] == val_attri1]
        no_records = df3.shape[0]  # Counting the number of records of the dataset

        occurrence_attri2 = df3[attri2].value_counts()[val_attri2]  # Calculating the number of occurrences of the specific value

        return occurrence_attri2/no_records

    def calc_MMRisk(userID,attri):
        # Calculates the Markov Model Risk for a given record by multiplying Start, Observation & Transition probabilities

        #attri1 = attri          # Assigning the passed attribute

        #index_attri1 = sensitive_attri.index(attri1)
        #attri2 = sensitive_attri[index_attri1 + 1]

        joint_p1 = calc_StartProbability(userID,attri) * calc_ObservationProbability(userID,attri)
        joint_p2 = 1
        for i in range(len(sensitive_attri)-1):

            attri1 = sensitive_attri[i]
            attri2 = sensitive_attri[i+1]

            joint_p2 *= calc_TransitionProbability(userID,attri1,attri2) * calc_ObservationProbability(userID,attri2)

        joint_prob = joint_p1 * joint_p2
        MMRisk = 1 - joint_prob
        MMRisk = round(MMRisk,3)        # Round off the value of MMRisk to 3 decimal points

        return MMRisk

    risk_list = []                      # List to store calculated risks for every index

    for i in range(df.shape[0]):            # Looping for every index
        risk_list.append(calc_MMRisk(i,sensitive_attri[0]))     # Starting from the first attribute


    print(risk_list)
    #risk_df = pd.DataFrame(risk_list, ['PR'])   # .T is used to obtain the transpose of the dataframe
    #print(risk_df)

    #return risk_df















