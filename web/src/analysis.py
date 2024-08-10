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
    Analyzes the data to identify trends related to safety.

    Parameters:
    - df (pd.DataFrame): The DataFrame to analyze.

    Returns:
    - pd.DataFrame: A DataFrame containing safety trends.
    """
    # Example: Grouping by a date column to find trends over time
    if 'date' in df.columns:
        trends = df.groupby(df['date'].dt.to_period('M')).sum()
        return trends
    else:
        raise ValueError("DataFrame must contain a 'date' column for trend analysis.")