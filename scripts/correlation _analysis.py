# scripts/correlation_analysis.py
import pandas as pd

def calculate_correlation(df, column1, column2):
    """Calculate and return correlation between two columns."""
    correlation = df[column1].corr(df[column2])
    return correlation

if __name__ == "__main__":
    df = pd.read_csv('data/news_with_returns.csv')
    correlation = calculate_correlation(df, 'polarity', 'Daily_Stock_Return')
    print(f'Correlation between sentiment intensity and stock returns: {correlation}')
