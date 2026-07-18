import pandas as pd 

def generate_report(file_path):
    df = pd.read_csv(file_path)
    return df.describe()