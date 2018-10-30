# -*- coding: utf-8 -*-

'''
This script downloads data from `CryptoCurrency Market Capitalizations`.
It filters for Ethereum data with a Market Cap.
Data is downloaded from https://coinmarketcap.com/tokens/views/all/
'''

__author__ = "wildlyclassyprince"
__license__ = "GNU"
__email__ = "lihtumb@gmail.com"

# The usual suspects ...
from datetime import datetime
import pandas as pd

# Data location
URL = https://coinmarketcap.com/rankings/exchanges/reported/

# Using Pandas to return the first table on the page
df = pd.read_html(URL, attrs={'id': 'exchange-rankings'})[0]

# Cleaning numeric data:
columns = [column in df.columns if df[column].dtypes == 'O']
columns.pop(0) # Drops from the list 'Name'
columns.pop(-1) # Drops from the list 'Launched'
for column in columns:
  df[column] = df[column].apply(lambda x: x.upper())
  df[column] = df[column].str.replace('$', '')
  df[column] = df[column].str.replace(',', '')
  df[column] = df[column].str.replace('Low Vol', '0')
  df[column] = df[column].str.replace('%', '')
  df[column] = df[column].str.strip()

# Drop 'Vol Graph (7d)'
df.drop('vol Graph (7d)', axis=1, inplace=True)

# Convert numeric columns to numeric type
def coerce_df_columns_to_numeric(df, column_list):
    '''Convert numeric columns to numeric type.'''
    df[column_list] = df[column_list].apply(pd.to_numeric, errors='coerce')

coerce_df_columns_to_numeric(df, columns)

# Convert date columns to date-time type
df['Launched'] = pd.to_datetime(df['Launched'])
