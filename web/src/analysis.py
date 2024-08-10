def get_summary_statistics(df):
    """
    Generates summary statistics for the DataFrame.

    Parameters:
    - df (pd.DataFrame): The DataFrame to analyze.

    Returns:
    - pd.DataFrame: A DataFrame containing the summary statistics.
    """
    return df.describe()