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
#from mmRisk_manySAs import create_Risk_Dataframe

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

    def get_correlation_df():
        ## This function generates a dataframe of correlation between each attributes.

        corr_list = []

        for attri2 in attributes:
            corr = []
            for attri1 in attributes:
                corr.append(calc_correlation(attri1, attri2))
            corr_list.append(corr)

        corr_df = pd.DataFrame(corr_list, columns=attributes, index=attributes)

        return corr_df

    def find_highest_correlation(corr_df,attri):
        ## Returns the mostly correlated attribute name with the passed 'attri' and related correlation value
                # Arguments :   corr_df     --> Pandas dataframe of correlations between attributes
                #               attri       --> An atrribute to find the highest correlation

        # Creates a series of correlation of the other attributes with the passed 'attri'
        corr_series = corr_df[attri]
        print('\nCorrelations')
        print(corr_series)

        # Get the index series when the correlations are sorted in descending order.
        # This is a numbering series without attribute names
        corr_indexes = corr_series.argsort()[::-1]

        corr_indexes_list = []  # List to store the exact names of attributes as sorted order

        # Assigning exact names of attributes to the list
        for ind in corr_indexes:
            corr_indexes_list.append(attributes[ind])

        # Highest correlated attribute is in the 2nd position of the list. (1st position is the same attribute)
        highest_correlated_attribute = corr_indexes_list[1]

        # Finding the highest correlation
        corr_list_sorted = corr_series.to_list()        # Converts the series of correlations to a list
        corr_list_sorted.sort(reverse = True)           # Sorting the list in descending order
        highest_correlation = corr_list_sorted[1]       # Highest correlation is in the 2nd position of the list.


        return highest_correlated_attribute,highest_correlation

    def get_ordered_correlation(corr_df,arr_o):

        corr_df_for_o = corr_df[arr_o]

        # Create a flattened DataFrame with values, index, and column names
        print(corr_df_for_o)
        flattened_df = corr_df_for_o.stack().reset_index()
        print(flattened_df)

        # Sort the flattened DataFrame in descending order of values
        sorted_df = flattened_df.sort_values(0, ascending=False)
        print(sorted_df)

        no_runs = len(attributes) * len(arr_o)

        ok = 0

        for i in range(no_runs):
            corr_val = sorted_df.iloc[i][0]
            a_i = sorted_df.iloc[i]['level_0']
            o_i = sorted_df.iloc[i]['level_1']

            if a_i != o_i:
                if a_i not in arr_o:
                    ok = a_i
                    break
        return ok







        '''
        # Extract the index and column names from the sorted DataFrame
        values = []
        index_names = []
        column_names = []

        for i in range(num_elements):
            value = sorted_df.iloc[i][0]
            index_name = sorted_df.iloc[i]['level_0']
            column_name = sorted_df.iloc[i]['level_1']

            values.append(value)
            index_names.append(index_name)
            column_names.append(column_name)
        '''

    ## 3. Finding the attribute which has the highest mean single attribute risk (o1)

    mean_sar_arr = calc_single_attribute_risks()         # A array with mean single attribute risk of all attributes
                                                        # Length = No of attributes
    #mean_sar_arr.sort(reverse=True)                      # Sorting the array for descending order
    #print(mean_sar_arr)

    mean_sar_series = pd.Series(mean_sar_arr,index = attributes)
    print('\nMean Single Attribute Risk Table')
    print(mean_sar_series)

    # Get the index series (Only index numbers) when the data is sorted in descending order
    mean_sar_series_indexes = mean_sar_series.argsort()[::-1]

    mean_sar_series_indexes_list = []           # List to store the exact names of attributes as sorted order

    # Assigning exact names of attributes to the list
    for ind in mean_sar_series_indexes:
        mean_sar_series_indexes_list.append(attributes[ind])

    print('\nMean Single Attribute Indexes after sorting')
    print(mean_sar_series_indexes_list)

    # Atrribute name having the highest single attribute mean risk
    o1 = mean_sar_series_indexes_list[0]

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


    ## Pre-requisite

    # Generate the dataframe of correlations
    corr_df = get_correlation_df()
    print('Correlation Table')
    print(corr_df)

    # Calculating 'm' ( = No of attributes)
    m = len(attributes)

    # Creating a list for 'O'
    arr_o = []
    arr_o.append(o1)



    for val in range (1,m):       # This for loop runs from i=1 to i=m-1
        print('====== For loop - val = '+str(val) + ' ================================= ')

        # a) Finding the attribute having the next highest single attribute risk
        print(mean_sar_series_indexes_list)
        print(arr_o)
        #oj = ''
        for ind in mean_sar_series_indexes_list:
            #print(ind)
            if ind not in arr_o:
                oj = ind
                break
        #print(mean_sar_series_indexes_list)
        print('Oj = ' + str(oj))

        # b) Finding the attribute having the highest correlation with any of attribute in O

        # A float to store the highest correlation values for each attributes in 'arr_o'
        max_corr_o = 0
        '''
        for attri in arr_o:
            highest_correlated_attribute, highest_correlation = find_highest_correlation(corr_df,attri)
            if highest_correlation > max_corr_o:
                max_corr_o = highest_correlation
            if highest_correlated_attribute not in arr_o:
                ok = highest_correlated_attribute
        '''
        '''
        arr_ok = []
        for attri in arr_o:
            arr_ok.append(find_highest_correlation(corr_df,attri))

        #print(arr_ok)
        ok_corr_df = pd.DataFrame(arr_ok, columns = ['highest_correlated_attribute', 'highest_correlation'])
        print(ok_corr_df)
        ok_corr_df_sorted = ok_corr_df.sort_values(by = ['highest_correlation'], ascending = False, ignore_index = True)
        print(ok_corr_df_sorted)

        for i in range(len(arr_o)):
            ok = ok_corr_df_sorted.iloc[0]['highest_correlated_attribute']
            if ok not in arr_o:
                break
        '''

        ok = get_ordered_correlation(corr_df,arr_o)

        #ok = 'a1'
        print('Ok = ' + str(ok))

        # Calculating PRmean for all the combinations of o1...oj attributes

        arr_with_oj = arr_o + oj.split()
        #print(arr_with_oj)
        combinations_j = find_attri_combinations(arr_with_oj)
        #print(combinations_j)
        max_pr_mean = 0
        max_combination = []

        for comb in combinations_j:
            pr_mean = calc_pr_mean(df, comb)
            if pr_mean > max_pr_mean:
                max_combination = list(comb)
                max_pr_mean = pr_mean

        # Calculating PRmean for all the permutations of o1...ok attributes

        arr_with_ok = arr_o + ok.split()
        combinations_k = find_attri_combinations(arr_with_ok)

        for comb in combinations_k:
            #print(comb)
            pr_mean = calc_pr_mean(df, comb)
            if pr_mean > max_pr_mean:
                max_combination = list(comb)
                max_pr_mean = pr_mean

        arr_o = max_combination

        print('O order = ' + str(arr_o))
        print('Max PR Mean = ' + str(max_pr_mean))
        print('\n')

        # If calculated PRmean > theta (privacy risk probability threshold) --> Break
        if max_pr_mean > theta:
            print('Max PR Mean > theta')
            break

    return arr_o










































