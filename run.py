import pandas as pd
from src.data_ingestion import load_data, save_data
from src.data_preprocessing import clean_data, transform_data
from src.analysis import get_summary_statistics, get_safety_trends
from src.visualization import plot_safety_trends
from src.model import train_model

# first to load the data
data_path = 'data/raw/safety_reports.csv'
df = load_data(data_path)

# next to preprocess the data
df = clean_data(df)
df = transform_data(df)

# next to analyze the data received
summary_stats = get_summary_statistics(df)
print(summary_stats)

trends = get_safety_trends(df)
plot_safety_trends(trends)

# time to train the model
# let's assume 'incident_severity' is the target variable and other colums as 
X = df.drop(columns=['incident_severity'])
y = df['incident_severity']
model = train_model(X, y)

processed_data_path = 'data/processed/cleaned_safety_reports.csv'
save_data(df, processed_data_path)

# my aim hee is to integrate all components in this script to run the asms system