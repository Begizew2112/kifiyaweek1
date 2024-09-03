# scripts/stock_returns.py
import pandas as pd

def calculate_stock_returns(df, price_column):
    """Calculate daily stock returns based on the specified price column."""
    df['Daily_Stock_Return'] = df[price_column].pct_change()
    df = df.dropna(subset=['Daily_Stock_Return'])  # Remove rows with missing values after pct_change calculation
    return df

if __name__ == "__main__":
    df = pd.read_csv('data/news_with_sentiment.csv')
    df = calculate_stock_returns(df, 'Close')
    df.to_csv('data/news_with_returns.csv', index=False)
