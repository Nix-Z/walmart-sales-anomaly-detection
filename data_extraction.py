import zipfile
import pandas as pd

def load_data():
  data = pd.read_csv('data.csv.zip', compression='zip')
  return data

load_data()
