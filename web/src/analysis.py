def get_summary_statistics(df):
    """
    Generates summary statistics for the DataFrame.

    Parameters:
    - df (pd.DataFrame): The DataFrame to analyze.

    Returns:
    - pd.DataFrame: A DataFrame containing the summary statistics.
    """
    return df.describe()

def get_safety_trends(df):
    """
    Analyzes safety trends from the DataFrame.

    Parameters:
    - df (pd.DataFrame): The DataFrame with safety data.

    Returns:
    - pd.DataFrame: The DataFrame with safety trends.
    """
    if 'incident_date' not in df.columns:
        raise ValueError("DataFrame must contain an 'incident_date' column for trend analysis.")

    # Example: Trend analysis based on 'incident_date'
    trends = df.groupby(df['incident_date'].dt.to_period('M')).size()

    return trends