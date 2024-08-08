import matplotlib.pyplot as plt

def plot_safety_trends(trends):
    """plan is to plot safety trends."""
    plt.figure(figsize=(10, 6))
    plt.plot(trends.index, trends.values, marker='o')
    # trends.plot(kind='bar')
    plt.title('Safety Trends Over Time')
    plt.xlabel('Year')
    plt.ylabel('Number of Incidents')
    # plt.savefig('plots/safety_trends.png') # to save the plotted graph to a file
    # plt.close() # to close the plot to free resources
    plt.grid(True)
    # plt.show()

    # saving the plot
    plt.savefig('plots/safety_trends.png') # to save the plotted graph to a file

    # show the plot
    plt.show()

# my aim here is to visualize the data to gain insights