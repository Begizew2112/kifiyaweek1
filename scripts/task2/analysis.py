import os
import pandas as pd
import matplotlib.pyplot as plt
from pypfopt import expected_returns, risk_models, EfficientFrontier
import ta

# Define the path to the data directory
data_directory = 'c:/Users/Yibabe/Desktop/kifiyaweek1/data'

# List of CSV filenames
csv_files = [
    'AAPL_historical_data.csv',
    'AMZN_historical_data.csv',
    'GOOG_historical_data.csv',
    'META_historical_data.csv',
    'MSFT_historical_data.csv',
    'NVDA_historical_data.csv',
    'TSLA_historical_data.csv'
]

# Create a dictionary to hold DataFrames
dfs = {}

# Load CSV files into DataFrames
for file in csv_files:
    file_path = os.path.join(data_directory, file)
    dfs[file] = pd.read_csv(file_path)

# Check the loaded DataFrames
for name, df in dfs.items():
    print(f"{name} head:\n{df.head()}\n")

# Define a function to calculate technical indicators
def calculate_technical_indicators(df):
    df['SMA_20'] = ta.trend.sma_indicator(df['Close'], window=20)
    df['RSI'] = ta.momentum.RSIIndicator(df['Close']).rsi()
    macd = ta.trend.MACD(df['Close'])
    df['MACD'] = macd.macd()
    df['MACD_Signal'] = macd.macd_signal()
    df['MACD_Hist'] = macd.macd_diff()
    return df

# Apply technical indicators to each DataFrame
for name, df in dfs.items():
    dfs[name] = calculate_technical_indicators(df)
    print(f"Technical indicators applied to {name}:\n{dfs[name].head()}\n")

# Define a function to calculate portfolio weights
def calculate_portfolio_weights(data):
    # Calculate expected returns and sample covariance matrix
    mu = expected_returns.mean_historical_return(data)
    cov = risk_models.sample_cov(data)

    # Optimize for maximum Sharpe ratio
    ef = EfficientFrontier(mu, cov)
    weights = ef.max_sharpe()

    # Get the cleaned weights and convert them to a dictionary
    cleaned_weights = ef.clean_weights()
    return cleaned_weights

# Combine all stock data into a single DataFrame
combined_data = pd.concat(dfs.values(), axis=1, join='inner')

# Calculate portfolio weights
weights = calculate_portfolio_weights(combined_data)

# Display the portfolio weights
print("Optimized Portfolio Weights:")
for ticker, weight in weights.items():
    print(f"{ticker}: {weight:.4f}")

# Define a function to calculate portfolio performance
def calculate_portfolio_performance(data, weights):
    # Calculate expected returns and sample covariance matrix
    mu = expected_returns.mean_historical_return(data)
    cov = risk_models.sample_cov(data)

    # Create an instance of Efficient Frontier
    ef = EfficientFrontier(mu, cov)

    # Set the portfolio weights
    ef.set_weights(weights)

    # Calculate the performance
    performance = ef.portfolio_performance(verbose=True)
    
    return performance

# Calculate and display the portfolio performance
performance = calculate_portfolio_performance(combined_data, weights)
print("Portfolio Performance:")
print(f"Expected annual return: {performance[0]:.2%}")
print(f"Annual volatility: {performance[1]:.2%}")
print(f"Sharpe ratio: {performance[2]:.2f}")
