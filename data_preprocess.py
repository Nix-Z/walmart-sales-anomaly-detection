import pandas as pd
from data_analysis import analyze_data

def preprocess_data():
    data = analyze_data()
    data['Date'] = pd.to_datetime(data['Date'], format="%Y-%m-%d")
    data.drop(['Unnamed: 0', 'Store'], axis=1, inplace=True)
    data.set_index('Date', inplace=True)
    print(data.head())

    return data

preprocess_data()
