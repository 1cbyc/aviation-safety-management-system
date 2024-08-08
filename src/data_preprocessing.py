import pandas as pd

def clean_data(df):
    """to perform data cleaning"""
    df.dropna(inplace=True) # simplify the data cleaning step
    return df

def transform_data(df):
    """transform data for analysis"""
    df['incident_date'] = pd.to_datetime(df['incident_date'])
    return df
