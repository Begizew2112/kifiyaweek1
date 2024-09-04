import os
import pandas as pd
import talib
import matplotlib.pyplot as plt

class StockDataAnalyzer:
    def __init__(self, data_directory, csv_files):

        self.data_directory = data_directory
        self.csv_files = csv_files
        self.dfs = {}  # Dictionary to hold DataFrames
    
    def load_data(self):
        #Loads CSV files into DataFrames and stores them in the dfs dictionary.
        for file in self.csv_files:
            file_path = os.path.join(self.data_directory, file)
            try:
                df = pd.read_csv(file_path)
                df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
                df = df.sort_values('Date')
                df = df.dropna(subset=['Date'])
                self.dfs[file] = df
                print(f"Loaded {file} successfully.")
            except Exception as e:
                print(f"Error loading {file}: {e}")
    
    def apply_technical_indicators(self):
        #Calculates technical indicators using TA-Lib for each DataFrame in the dfs dictionary.
        for name, df in self.dfs.items():
            try:
                df['Close'] = df['Close'].astype(float)
                df['SMA_20'] = talib.SMA(df['Close'], timeperiod=20)
                df['RSI'] = talib.RSI(df['Close'], timeperiod=14)
                df['MACD'], df['MACD_Signal'], df['MACD_Hist'] = talib.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
                df = df.dropna()
                self.dfs[name] = df
                print(f"Technical indicators applied to {name}.")
            except Exception as e:
                print(f"Error applying technical indicators to {name}: {e}")
    
    def visualize_data(self):
        #Visualizes the stock data and technical indicators for each DataFrame.
        for name, df in self.dfs.items():
            if 'Date' not in df.columns:
                print(f"Skipping {name}: 'Date' column not found.")
                continue
            
            # Plot Close Price, SMA, and Volatility
            plt.figure(figsize=(14, 7))
            plt.subplot(2, 1, 1)
            plt.plot(df['Date'], df['Close'], label='Close Price')
            plt.plot(df['Date'], df['SMA_20'], label='20-Day SMA', linestyle='--')
            plt.title(f'{name} Stock Price and 20-Day SMA')
            plt.xlabel('Date')
            plt.ylabel('Price')
            plt.legend()

            plt.subplot(2, 1, 2)
            plt.plot(df['Date'], df['RSI'], label='RSI', color='purple')
            plt.axhline(70, color='red', linestyle='--', linewidth=1)
            plt.axhline(30, color='green', linestyle='--', linewidth=1)
            plt.title(f'{name} RSI')
            plt.xlabel('Date')
            plt.ylabel('RSI')
            plt.legend()
            plt.tight_layout()
            plt.show()

            # MACD Plot
            plt.figure(figsize=(14, 7))
            plt.plot(df['Date'], df['MACD'], label='MACD', color='blue')
            plt.plot(df['Date'], df['MACD_Signal'], label='MACD Signal', color='orange', linestyle='--')
            plt.bar(df['Date'], df['MACD_Hist'], label='MACD Histogram', color='grey', alpha=0.3)
            plt.title(f'{name} MACD')
            plt.xlabel('Date')
            plt.ylabel('MACD Value')
            plt.legend()
            plt.show()

    def save_dataframes(self, output_directory):
        #Saves each DataFrame in the dfs dictionary to a CSV file.
        os.makedirs(output_directory, exist_ok=True)
        for name, df in self.dfs.items():
            output_path = os.path.join(output_directory, f"cleaned_{name}")
            df.to_csv(output_path, index=False)
            print(f"Saved {name} to {output_path}")

def main():
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

    # Initialize the StockDataAnalyzer
    analyzer = StockDataAnalyzer(data_directory, csv_files)

    # Load data
    analyzer.load_data()

    # Apply technical indicators
    analyzer.apply_technical_indicators()

    # Visualize data
    analyzer.visualize_data()

    # Save cleaned data
    output_directory = 'c:/Users/Yibabe/Desktop/kifiyaweek1/output'
    analyzer.save_dataframes(output_directory)

if __name__ == "__main__":
    main()
