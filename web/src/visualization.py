import matplotlib.pyplot as plt

def plot_safety_trends(trends, save_path):
    """to plot the safety trends over time and save"""
    plt.figure(figsize=(10, 6))
    # plt.plot(trends.index, trends.values, marker='o')
    plt.plot(trends['date'], trends['incident_count'], marker='o', linestyle='-')
    plt.title('Safety Trends Over Time')
    # plt.xlabel('Year')
    plt.xlabel('Date')
    plt.ylabel('Number of Incidents')
    plt.grid(True)

    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()

    plt.close()
    # # to save the plot
    # plt.savefig(save_path)
    #
    # # not needed but can be used to show the plot if running locally
    # plt.show()