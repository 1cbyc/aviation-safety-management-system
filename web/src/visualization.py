import matplotlib.pyplot as plt

def plot_safety_trends(trends, save_path=None):
    print(f"plot_safety_trends called with trends:")
    plt.figure(figsize=(10, 6))
    plt.plot(trends['date'], trends['incident_count'], marker='o', linestyle='-')
    plt.title('Safety Trends Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Incidents')
    plt.grid(True)

    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()

    plt.close()