import matplotlib.pyplot as plt

def plot_safety_trends(trends):
    """plan is to plot safety trends."""
    plt.figure(figsize=(10, 6))
    trends.plot(kind='bar')
    plt.title('Safety Trends Over Time')
    plt.xlabel('Year')
    plt.ylabel('Number of Incidents')
    plt.show()

# my aim here is to visualize the data to gain insights