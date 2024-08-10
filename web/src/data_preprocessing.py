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
    else:
        raise ValueError("DataFrame must contain an 'incident_date' column for transformation.")

    # Example transformation: Encoding categorical variables
    df = pd.get_dummies(df, drop_first=True)

    return df