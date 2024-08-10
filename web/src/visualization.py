import matplotlib.pyplot as plt


def plot_safety_trends(trends, save_path=None):
    """
    Plots safety trends and optionally saves the plot.

    Parameters:
    - trends (pd.DataFrame): The DataFrame containing trends to plot.
    - save_path (str, optional): The path where the plot should be saved.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(trends.index, trends, marker='o', linestyle='-', color='b')
    plt.title('Safety Trends Over Time')
    plt.xlabel('Date')
    plt.ylabel('Incidents')
    plt.grid(True)

    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()