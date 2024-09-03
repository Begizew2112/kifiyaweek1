# scripts/data_preprocessing.py
import pandas as pd

def merge_data(stock_file, news_file):
    """Merge stock data with news data on a common date column."""
    stock_df = pd.read_csv(stock_file)
    news_df = pd.read_csv(news_file)
    
    # Clean unnecessary columns if needed
    stock_df = stock_df[['Date', 'Close']]  # Keep only relevant columns
    news_df = news_df[['date', 'headline']]  # Keep only relevant columns
    
    # Merge data on 'Date' and 'date' columns
    merged_df = pd.merge(stock_df, news_df, left_on='Date', right_on='date', how='inner')
    
    return merged_df

if __name__ == "__main__":
    merged_df = merge_data('data/AAPL_historical_data.csv', 'data/processed_analyst_ratings.csv')
    merged_df.to_csv('data/merged_data.csv', index=False)
