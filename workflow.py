'''
This workflow finds the ordered attributes o1,⋯, om that gives the highest mean, median, maximum or marketer risk.
The same workflow is applicable to calculate the worst-case median,marketer, and maximum risks as well

only considers the potential combinations that would give the highest risk and prunes the unnecessary combinations
of attributes with lower risks.
'''
import pandas as pd
import scipy.stats as stats
import numpy as np
from itertools import permutations
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

        return single_attribute_risks


    ## 2. Calculate the correlation scores between attributes
    def calc_correlation(attri1, attri2):
        # ' This returns the Cramer's V Correlation scores between the given attributes of attri1 & attri2

        contingency_table = pd.crosstab(df[attri1], df[attri2])
        arr = contingency_table.to_numpy()

        # Chi-squared test statistic, sample size, and minimum of rows and columns
        x2 = stats.chi2_contingency(arr, correction=False)[0]

        n = np.sum(arr)
        min_dim = min(arr.shape) - 1

        # calculate Cramer's V
        v = np.sqrt((x2 / n) / min_dim)

        return v

    corr_list = []

    for attri2 in attributes:
        corr = []

        for attri1 in attributes:
            corr.append(calc_correlation(attri1,attri2))
        corr_list.append(corr)

    corr_df = pd.DataFrame(corr_list, columns = attributes, index = attributes)

    print(corr_df)

    ## 3. Finding the attribute which has the highest mean single attribute risk (o1)

    arr = calc_single_attribute_risks()         # A array with mean single attribute risk of all attributes
                                                # Length = No of attributes
    sort_arr = arr.sort()                       # Sorting the array for descending order

    max_single_attri_risk = sort_arr[0]  # Highest single attribute mean risk = 1st element of the sorted array

    # Atrribute name having the highest single attribute mean risk
    o1 = attributes[arr.index(max_single_attri_risk)]

    print(max_single_attri_risk)
    print(o1)

    ## 4. Finding o(i+1) from i = 2 to i = m-1


    def find_attri_combinations(attributes):
        # This function finds all the attribute combinations (without symetry) with all elements in 'attributes'

        #Length of the attributes list
        length_combinations = len(attributes)

        # Generate all the shuffled combinations of the elements (With all elements) of the attribute list
        all_combinations = list(permutations(attributes, length_combinations))

        # A list for storing the combinations excluding symmetric
        combinations_without_symm = []

        # Checking for the list with its reversed lists
        for comb in all_combinations:
            if comb not in combinations_without_symm and comb[::-1] not in combinations_without_symm:
                combinations_without_symm.append(comb)

        return combinations_without_symm

    arr_o = []
    arr_o.append(o1)
    m = len(attributes)

    for val in range (1,m):       # This for loop runs from i=1 to i=m-1
        # a) Finding the attribute having the next highest single attribute risk
        oj = sort_arr[val]

        # b) Finding the attribute having the highest correlation with oi
        corr_series = corr_df[arr_o[val]]

        # Get the index series when the data is sorted in descending order
        descending_indexes = corr_series.argsort()[::-1]

        # Convert the index series to a list
        descending_indexes_list = descending_indexes.tolist()

        ok = descending_indexes_list[val]

        # Calculating PRmean for all the permutations of o1...oj attributes
        sar_oj = 0

        # Calculating PRmean for all the permutations of o1...oj attributes
        sar_ok = 0

        # Appending the array of 'o' with the attribute with higher single attribute risk

        if sar_oj >= sar_ok:
            arr_o.append(oj)
        else:
            arr_o.append(ok)

    return arr_o

















        ok =

        print(descending_indexes_list)












        ok = 1


























