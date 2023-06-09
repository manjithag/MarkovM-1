### Markov Model Risk Calculation with and without duplicates of users
### Valid for many (more than 2) attributes
### This is dedicated for the workflow which finds the ordered attributes o1, o2,⋯, om that gives the highest mean risk.

import pandas as pd
def calc_pr_mean(df:pd.DataFrame,sensitive_attri:list):

    """
    Calculate a dataframe with the values of risk of re-identification for each record (users / index)
        INPUTS  : df = Original dataset : Pandas dataframe
                  sensitive_attri = Column names of sensitive attributes : List
        RETURN  : mean risk of any record in the dataset being re-identified
    """


    def calc_start_probability(index,attri):
        # Calculate the start probability of a given attribute and index --> P(attri = attri_val)

        no_records = df.shape[0]        # Counting the number of records of the dataset
        attri_val = df.loc[index][attri]      # Obtaining the value of the given attribute for the given index
        occurrence = df[attri].value_counts()[attri_val]      # Calculating the number of occurrences of the specific value

        return occurrence/no_records           # Returning start probability

    def calc_observation_probability(index,attri):
        # Calculate the observation probability of a given attribute and index
        # --> 1 - P(user = attri_val / attri = attri_val)

        attri_val = df.loc[index][attri]
        userID  = df.loc[index]['userID']

        df2 = df.loc[df[attri] == attri_val]
        no_records = df2.shape[0]            # Counting the number of records of the dataset

        occurrence = df2['userID'].value_counts()[userID]  # Calculating the number of occurences of the specific value

        return (1-occurrence/no_records)        # Returning observation probability

    def calc_transition_probability(index,attri1,attri2):
        # Calculates the transition probability from given attribute to next attribute
        # --> P(attri2 = attri2_val / attri1 = attri1_val)

        val_attri1 = df.loc[index][attri1]
        val_attri2 = df.loc[index][attri2]

        df3 = df.loc[df[attri1] == val_attri1]
        no_records = df3.shape[0]  # Counting the number of records of the dataset

        occurrence_attri2 = df3[attri2].value_counts()[val_attri2]  # Calculating the number of occurrences of the specific value

        return occurrence_attri2/no_records     # Returning transition probability

    def calc_mm_risk(userID,attri):
        # Calculates the Markov Model Risk for a given record by multiplying Start, Observation & Transition probabilities

        joint_p1 = calc_start_probability(userID,attri) * calc_observation_probability(userID,attri)
        joint_p2 = 1
        for i in range(len(sensitive_attri)-1):

            attri1 = sensitive_attri[i]
            attri2 = sensitive_attri[i+1]

            joint_p2 *= calc_transition_probability(userID,attri1,attri2) * calc_observation_probability(userID,attri2)

        joint_prob = joint_p1 * joint_p2
        mm_risk = 1 - joint_prob
        mm_risk = round(mm_risk,5)        # Round off the value of MMRisk to 3 decimal points

        return mm_risk

    risk_list = []                      # List to store calculated risks for every index
    for i in range(df.shape[0]):            # Looping for every index
        risk_list.append(calc_mm_risk(i,sensitive_attri[0]))     # Starting from the first attribute

    #print(risk_list)
    risk_df = pd.DataFrame(risk_list, columns = ['PR']).T   # .T is used to obtain the transpose of the dataframe

    ## Metrices calculation for the whole dataset

    pr_min = min(risk_list)
    pr_max = max(risk_list)
    pr_mean = sum(risk_list)/len(risk_list)
    pr_mean = round(pr_mean,5)

    # Calculating PR median
    risk_list.sort()
    mid = len(risk_list) // 2
    pr_median = (risk_list[mid] + risk_list[mid-1]) / 2
    pr_median = round(pr_median,5)

    # Calculating Marketer Risk
    # Marketer Risk = (No of records with risk of 1) / (total records)
    pr_marketer = risk_list.count(1) / len(risk_list)

    print( 'Attribute Comb = ' + str(sensitive_attri) + '  -  PR mean = ' + str(pr_mean))

    return pr_mean















