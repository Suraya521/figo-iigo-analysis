import pandas as pd

def calculate_score(path):
    df = pd.read_csv(path)
    return df.describe()
