import pandas as pd

def clean_data(df):
    """to perform data cleaning"""
    df.dropna(inplace=True) # simplify the data cleaning step
    return df

def transform_data(df):
    """transform data for analysis"""
    # convert the incident_date to datetime
    df['incident_date'] = pd.to_datetime(df['incident_date'])
    # to create a new column for the numerical representation of incident 
    df['incident_date'] = pd.to_datetime(df['incident_date']).apply(lambda x: x.toordinal())
    return df

# my aim here is to prepare data for analysis by cleaning, transforming and also handling the missing values.

# now i added  a step to convert the incident_date to a numerical format: