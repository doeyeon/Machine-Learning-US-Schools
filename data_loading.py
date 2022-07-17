'''
data_loading.py
Description:
A module to load in data.
Authors:
    Brandon Niles (180946050)
    Tony Yoon (170475670)
Purpose:
    To modify and load in different CSV datatypes for the purpose of analyzing.
Instructions:
    Import where needed
'''

#Imports
import pandas as pd

#Constants
removable_columns = ["Row", "FICE", "Name", "Postal", "Indicator", "Average Math SAT Score", "Average Verbal SAT Score",
    "Average Combined SAT Score", "Average ACT Score", "First Quartile Math SAT", "Third Quarter Math SAT", "First Quartile Verbal SAT",
    "Third Quartile Verbal SAT", "First Quartile ACT", "Third Quartile ACT", "Top 10 percent HS", "Top 25 percent HS", "Room Costs",
    "Board Costs", "Additional Fees", "Percent Alumni Donate"] #an array of columns to be removed from usnews.csv

#Methods

'''
make_tree_data(filename)
Fetches and internally modifies data from a given filename
Arguments:
    filename -> string: path of file
Returns:
    data -> dataframe: modified data
'''
def make_tree_data(filename):
    data = pd.read_csv(filename) #fetch dataframe
    data = data.drop(columns=removable_columns) #remove specified columns

    '''
    for key1, row in enumerate(data):
        for key2, item in enumerate(row):
            if item == "*":
                data[key1][key2] = "NaN" #replace * with NaN for later removal
    Was easier to just do this manually, but could also be automated.
    Unlikely that all datasets will contain asterisks for missing values 
    '''
    

    data = data.dropna() #removes all rows with NaN entries
    data.reset_index(drop=True, inplace=True) #fix row indices after removing problematic rows

    data['Graduation Rate'] = data['Graduation Rate'].apply(lambda x: "True" if x >= 50 else "False") #change majority graduation entries to either true or false
    data.rename(columns = {"Graduation Rate": "Majority Passing"}, inplace=True) #rename the column
    return(data)

