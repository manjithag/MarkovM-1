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
from mmrisk_for_workflow import calc_pr_mean


def find_workflow(df : pd.DataFrame, attributes : list, theta : float):
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

        #single_attribute_risks = [round(num, 4) for num in single_attribute_risks]

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

    def get_correlation_df():
        ## This function generates a dataframe of correlation between each attributes in the dataframe.

        corr_list = []

        for attri2 in attributes:
            corr = []
            for attri1 in attributes:
                corr.append(calc_correlation(attri1, attri2))
            corr_list.append(corr)

        corr_df = pd.DataFrame(corr_list, columns=attributes, index=attributes)

        return corr_df

    def get_highest_correlated_attri(corr_df,arr_o):

        # Creates a dataframe with correlations for attributes in 'arr_o' with all the attributes
        corr_df_for_o = corr_df[arr_o]
        print('Correlations for attributes in O = ' + str(arr_o) + ' with all the attributes')
        print(corr_df_for_o)

        # Create a flattened DataFrame with values, index, and column names
            # Column name : level_0 --> for the attributes in 'attributes'
            # Column name : level_1 --> for the attributes in 'arr_o'
        flattened_corr_df = corr_df_for_o.stack().reset_index()

        # Sort the flattened DataFrame in descending order of correlation values
        sorted_corr_df = flattened_corr_df.sort_values(0, ascending=False)
        print('\nFlattened and sorted correlations')
        print(sorted_corr_df)

        # Calculate the number of rows in 'sorted_df'
        no_runs = len(attributes) * len(arr_o)

        # Check all the records to find 'ok'
        # ok is the attribute having the highest correlation with one of the attribute in 'arr_o'
        # But it should not be already available in 'arr_o'
        for i in range(no_runs):
            a_i = sorted_corr_df.iloc[i]['level_0']    # Column name : level_0 --> for the attributes in 'attributes'
            o_i = sorted_corr_df.iloc[i]['level_1']    # Column name : level_1 --> for the attributes in 'arr_o'

            # If a_i = o_i , it gives correlations of 1 since both are same attribute. So a_i != o_i is considered.
            if a_i != o_i:
                if a_i not in arr_o:        # 'ok' should not be already available in 'arr_o'
                    ok = a_i
                    break
        return ok


    ## 3. Finding the attribute which has the highest mean single attribute risk (o1)

    # Creates a list with mean single attribute risk of all attributes
    # Length = No of attributes
    mean_sar_arr = calc_single_attribute_risks()

    # Creates a pandas series with mean single attribute risk of all attributes with the index of attribute names
    mean_sar_series = pd.Series(mean_sar_arr,index = attributes)
    print('\nMean Single Attribute Risk Table')
    print(mean_sar_series)

    # Get the index series (Only index numbers) when the mean single attribute risks are sorted in the descending order
    mean_sar_series_indexes = mean_sar_series.argsort()[::-1]

    # List to store the exact names of attributes as sorted order
    mean_sar_series_indexes_list = []

    # Assigning exact names of attributes to the list
    for ind in mean_sar_series_indexes:
        mean_sar_series_indexes_list.append(attributes[ind])

    print('\nAttribute order after sorting = ' + str(mean_sar_series_indexes_list))

    # Finding 'o1' which is the atrribute name having the highest single attribute mean risk
    o1 = mean_sar_series_indexes_list[0]
    print('O1 = ' + str(o1))

    def find_attri_combinations(attri_list : list):
        # This function finds all the attribute combinations (without reversed) with all elements in 'attri_list'
        # Ex : Original combination = ['a', 'c', 'b']   Reversed combination = ['b', 'c', 'a']

        # Length of the 'attri_list'
        length_combinations = len(attri_list)

        # Generate all the shuffled combinations of the elements (With all elements) of 'attri_list' as a list
        # This includes both original and reversed combination
        all_combinations = list(permutations(attri_list, length_combinations))

        # A list for storing the combinations excluding reversed combination
        combinations_without_symm = []

        # Storing the combinations excluding reversed combinations
        for comb in all_combinations:
            if comb not in combinations_without_symm and comb[::-1] not in combinations_without_symm:
                combinations_without_symm.append(comb)

        return combinations_without_symm


    ## Pre-requisite

    # Generate the dataframe of correlations
    corr_df = get_correlation_df()
    print('\nCorrelation Table')
    print(corr_df)

    # Calculating 'm' ( = No of attributes)
    m = len(attributes)

    # Creating a list for 'O'
    arr_o = []

    #Add found 'o1' as the first element of 'arr_o'
    arr_o.append(o1)

    ## Repetitive calculations to find o2, o3, o4.....
    # This for loop runs from i=1 to i=m-1
    for val in range (1,m):

        print('\n====== Finding o'+str(val+1) + ' =========================================== ')
        print('Array of O elements = ' + str(arr_o))

        ## a) Finding the attribute having the next highest single attribute risk
        for ind in mean_sar_series_indexes_list:
            if ind not in arr_o:
                oj = ind
                break

        print('Oj = ' + str(oj))

        ## b) Finding the attribute having the highest correlation with any of attribute in O

        ok = get_highest_correlated_attri(corr_df,arr_o)

        print('\nOk = ' + str(ok) + '\n')

        ## c) Calculating PRmean for all the combinations of o1...oj attributes

        # Create a list adding 'oj' to 'arr_o' to find the possible combinations
        arr_with_oj = arr_o + oj.split()
        combinations_j = find_attri_combinations(arr_with_oj)

        max_pr_mean = 0         # A float to store the maximum PRmean of all the combinations
        max_combination = []    # A list to store the attribute combination with maximum PRmean

        for comb in combinations_j:
            pr_mean = calc_pr_mean(df, comb)
            if pr_mean > max_pr_mean:
                max_combination = list(comb)
                max_pr_mean = pr_mean

        ## d) Calculating PRmean for all the permutations of o1...ok attributes

        # Create a list adding 'ok' to 'arr_o' to find the possible combinations
        arr_with_ok = arr_o + ok.split()
        combinations_k = find_attri_combinations(arr_with_ok)

        for comb in combinations_k:
            pr_mean = calc_pr_mean(df, comb)
            if pr_mean > max_pr_mean:
                max_combination = list(comb)
                max_pr_mean = pr_mean

        arr_o = max_combination

        print('\nNew array of O elements = ' + str(arr_o))
        print('Max PR Mean = ' + str(max_pr_mean))
        print('\n')

        # If calculated PRmean > theta (privacy risk probability threshold) --> Break
        if max_pr_mean > theta:
            print('Max PR Mean > theta')
            break

    return arr_o










































