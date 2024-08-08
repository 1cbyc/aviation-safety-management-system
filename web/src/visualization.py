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

    # what i did: the save_path param used is cause the plot_safety_trends function now accepts an optional save_path parameter. so if this parameter is provided, the plot is saved to the specified path. If it's not provided, the plot is displayed using plt.show().