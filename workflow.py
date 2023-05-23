'''
This workflow finds the ordered attributes o1,⋯, om that gives the highest mean, median, maximum or marketer risk.
The same workflow is applicable to calculate the worst-case median,marketer, and maximum risks as well

only considers the potential combinations that would give the highest risk and prunes the unnecessary combinations
of attributes with lower risks.
'''
import pandas as pd
from mmRisk_manySAs import create_Risk_Dataframe

def find_workflow(df : pd.DataFrame, attributes : list):
    ## This finds the ordered attributes o1,⋯, om that gives the highest mean, median, maximum or marketer risk.

    ## 1. Calculate the single attribute risks
    def calc_single_attribute_risks():
        # Calculate the single attribute risks of a given attribute list

        no_records = df.shape[0]        # Counting the number of records of the dataset
        single_attribute_risks = []

        for i in attributes:
            start_prob = 0

            for j in range (no_records):
                attri_val = df.loc[j][i]              # Obtaining the value of the given attribute for the given index
                occurrence = df[i].value_counts()[attri_val]     # Calculating the number of occurrences of the specific value
                start_prob += occurrence / no_records       # Returning start probability

            single_attribute_risks.append(start_prob/no_records)   # Appending with mean single attribute risk

        single_attribute_risks = [round(num, 4) for num in single_attribute_risks]
        max_single_attri_risk = max(single_attribute_risks)     # Highest single attribute mean risk

        # Atrribute name having the highest single attribute mean risk
        attribute_with_max_risk = attributes[single_attribute_risks.index(max_single_attri_risk)]

        print(single_attribute_risks)
        print(max_single_attri_risk)
        print(attribute_with_max_risk)

    calc_single_attribute_risks()

    ## 1. Calculate the correlation scores between attributes
    def calc_correlation():
        # ' This returns the Cramer's V Correlation scores between the given attributes of attri1 & attri2
        pass









