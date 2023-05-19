## MM Risk Calculation with duplicates of users ##
import pandas as pd
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
    #val = df2.loc[index, attri]         # Obtaining the value of the given attribute and given userID

    occurrence = df2['userID'].value_counts()[userID]  # Calculating the number of occurences of the specific value

    return (1-occurrence/no_records)

def calc_TransitionProbability(index,attri):
    # Calculates P(vj+1/vj )

    attri1 = attri              # Assigning the passed attribute (The attribute relevant to the risk of re-identification

    for i in sensitive_attri:  # Assigning the other attribute
        if attri1 != i:
            attri2 = i

    val_attri1 = df.loc[index][attri1]
    val_attri2 = df.loc[index][attri2]

    df3 = df.loc[df[attri1] == val_attri1]
    no_records = df3.shape[0]  # Counting the number of records of the dataset

    occurrence_attri2 = df3[attri2].value_counts()[val_attri2]  # Calculating the number of occurrences of the specific value

    return occurrence_attri2/no_records

def calc_MMRisk(userID,attri):
    attri1 = attri          # Assigning the passed attribute

    for i in sensitive_attri:      # Assigning the other attribute
        if attri1 != i:
          attri2 = i

    MMProb = calc_StartProbability(userID,attri1)*calc_ObservationProbability(userID,attri1)*calc_TransitionProbability(userID,attri1)*calc_ObservationProbability(userID,attri2)
    MMRisk = 1 - MMProb

    MMRisk = round(MMRisk,3)        # Round off the value of MMRisk to 3 decimal points

    return MMRisk



