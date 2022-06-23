import pandas as pd

'''
aaup.csv to dataframe
'''

aaup = pd.read_csv('aaup.csv')

# for i in aaup.loc[10,:]:  --> prints all the values for row 11 of the data set
#     print(i)

'''
usnews.csv to dataframe
'''
usnews = pd.read_csv('usnews.csv')
print(usnews.columns.tolist())