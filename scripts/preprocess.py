import pandas as pd

def load_and_preprocess_data(file_path):
    df = pd.read_csv(file_path)
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['date'] = df['date'].dt.tz_localize(None)  # Remove timezone information
    df.to_csv('preprocessed_data.csv', index=False)  # Save preprocessed data
    return df
