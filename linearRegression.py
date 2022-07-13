import pandas as pd
import numpy as np
import plotly.express as px
from scipy import stats

'''
Prepare data for linear regression. This includes:

1. Linear assumptions (dependant vs. independant)
2. Removing noise (outliers)
3. Removing collinearity 
4. Transforming into Gaussian Distribution
5. Normalize inputs
'''

# Clean up data by removing incomplete entries. Any row with null values will not be considered for linear regression.
# Initial dataset has 1161 data entries. After dropping incomplete data, we have 1074 data entries with no null values.
df1 = pd.read_csv('aaup.csv')
print(len(df1.index))
df2 = df1.dropna()
print(len(df2.index))

# Remove outliers in the dependant (y) variable. Find outliers for the different comps and remove said outliers.

# Visualize outliers for Full Professor Comp, Associate Professor Comp, Assistant Professor Comp, All Rank Comp
'''
# Full Professor Comp
fig = px.histogram(df2, x='Full Professor Comp', nbins=100,
                   text_auto=True, title='Count of Full Professor Compensations')
fig.show()

# Associate Professor Comp
fig = px.histogram(df2, x='Associate Professor Comp', nbins=100,
                   text_auto=True, title='Count of Associate Professor Compensations')
fig.show()

# Assistant Professor Comp
fig = px.histogram(df2, x='Assistant Professor Comp', nbins=100,
                   text_auto=True, title='Count of Assistant Professor Compensations')
fig.show()

# All Rank Comp
fig = px.histogram(df2, x='All Rank Comp', nbins=100,
                   text_auto=True, title='Count of All Rank Compensations')
fig.show()
'''

# Computes Z-score of each respective column, and removes rows with Z-scores above 3. 1058 data entries now.
df3 = df2[(np.abs(stats.zscore(df2['Full Professor Comp'])) < 3)]
df3 = df3[(np.abs(stats.zscore(df3['Associate Professor Comp'])) < 3)]
df3 = df3[(np.abs(stats.zscore(df3['Assistant Professor Comp'])) < 3)]
df3 = df3[(np.abs(stats.zscore(df3['All Rank Comp'])) < 3)]
print(len(df3.index))

corr_data = df3.corr(method='pearson')
corr_data.to_csv("Correlation Coefficients.csv", encoding='utf-8', index=True)
