import pandas as pd

def clean_data(df):
    df.dropna(inplace=True)
    return df

def transform_data(df):
    # Example transformation
    df['incident_date'] = pd.to_datetime(df['incident_date'])
    return df
