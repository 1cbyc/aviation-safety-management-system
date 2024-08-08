import pandas as pd

def get_summary_statistics(df):
    """to return summary stats of the dataframe"""
    return df.describe()

def get_safety_trends(df):
    """to identify safety trends over time"""
    # now to ensure the incident_data column is in datetime format
    df['incident_date'] = pd.to_datetime(df['incident_date'])
    trends = df.groupby(df['incident_date'].dt.year).size()
    return trends

# my aim here is to analyze and identify trends and risk factors