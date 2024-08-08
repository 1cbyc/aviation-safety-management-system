import os
import pandas as pd
from src.data_ingestion import load_data, save_data
from src.data_preprocessing import clean_data, transform_data
from src.analysis import get_summary_statistics, get_safety_trends
from src.visualization import plot_safety_trends
from src.model import train_model

# let's define data path first
data_path = 'data/raw/safety_reports.csv'

# then check if the file even exists
if not os.path.exists(data_path):
    raise FileNotFoundError(f"The file {data_path} does not exist. Please provide the correct file path.")

# then load the data
# data_path = 'data/raw/safety_reports.csv'
df = load_data(data_path)

# next to preprocess the data
df = clean_data(df)
df = transform_data(df)

# next to analyze the data received
summary_stats = get_summary_statistics(df)
print(summary_stats)

trends = get_safety_trends(df)

# now create plots directory if it does not exist
if not os.path.exists('plots'):
    os.makedirs('plots')

plot_safety_trends(trends)

# time to train the model
# in this case 'incident_severity' is the target variable and other columns as features
# X = df.drop(columns=['incident_severity'])
X = df.drop(columns=['incident_severity', 'incident_date'])
y = df['incident_severity']
model = train_model(X, y)

# then save the processed data
processed_data_path = 'data/processed/cleaned_safety_reports.csv'
save_data(df, processed_data_path)

# my aim hee is to integrate all components in this script to run the asms system