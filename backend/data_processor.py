import pandas as pd

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)
    df['date'] = pd.to_datetime(df['date'])
    df.fillna(0, inplace=True)
    return df
