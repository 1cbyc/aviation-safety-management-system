import pandas as pd


def clean_data(df):
    """
    Cleans the data by handling missing values and duplicates.

    Parameters:
    - df (pd.DataFrame): The DataFrame to clean.

    Returns:
    - pd.DataFrame: The cleaned DataFrame.
    """
    # Handle missing values
    df = df.dropna()

    # Remove duplicates
    df = df.drop_duplicates()

    return df


def transform_data(df):
    """
    Applies transformations to the data, such as encoding and normalization.

    Parameters:
    - df (pd.DataFrame): The DataFrame to transform.

    Returns:
    - pd.DataFrame: The transformed DataFrame.
    """
    # Example transformation: Converting dates to datetime format
    if 'incident_date' in df.columns:
        df['incident_date'] = pd.to_datetime(df['incident_date'])

    # Example transformation: Encoding categorical variables
    df = pd.get_dummies(df, drop_first=True)

    return df