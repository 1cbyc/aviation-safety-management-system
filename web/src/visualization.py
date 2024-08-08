import matplotlib.pyplot as plt

def plot_safety_trends(trends, save_path):
    """to plot the safety trends over time and save"""
    plt.figure(figsize=(10, 6))
    plt.plot(trends.index, trends.values, marker='o')
    plt.title('Safety Trends Over Time')
    plt.xlabel('Year')
    plt.ylabel('Number of Incidents')
    plt.grid(True)

    # to save the plot
    plt.savefig(save_path)

    # not needed but can be used to show the plot if running locally
    plt.show()