import pandas as pd

def load_data(file_path):
    """to load data from any csv file."""
    return pd.read_csv(file_path)

def save_data(df, file_path):
    """to save dataframe to a csv file"""
    df.to_csv(file_path, index=False)
