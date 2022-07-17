'''
test_data.py
Description:
A module to test the loading of data
Author:
    Brandon Niles (180946050)
Purpose:
    To demonstrate the importance of omitting certain columns from data
Instructions:
    Run file
'''

#Imports

from data_loading import make_tree_data
import pandas as pd

#Methods

'''
test_modify_data(filename)
Tests and demonstrates the importance of the make_tree_data() method
Arguments:
    filename -> string: path of file
Returns:
    None
Outputs:
    Text based on interpreted data
'''
def test_modify_data(filename):
    data = pd.read_csv(filename) #default data
    data2 = data.dropna() #remove missing values from default data
    data3 = make_tree_data(filename) #remove missing values AFTER removing problematic columns

    print("\n\n") #some spacing to make it easier to read
    print("{} has {} columns and {} rows.".format(filename, len(data.columns), len(data))) #default data
    print("If we remove rows with missing values we get {} columns and {} rows".format(len(data2.columns), len(data2)))
    print("However, if we first remove problematic columns (consistantly missing values among rows), we get:")
    print("{} columns and {} rows".format(len(data3.columns), len(data3)))
    print("Thus we have {} more entries to analyze without causing issues with missing data".format(len(data3) - len(data2)))
    print("\n\n")

#Driver Code
test_modify_data("data/usnews.csv")

