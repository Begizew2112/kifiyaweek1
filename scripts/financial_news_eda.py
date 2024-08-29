import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """
    Load data from a CSV file and handle potential issues with data loading.
    """
    try:
        # Load data from CSV
        df = pd.read_csv(file_path)

        # Convert 'date' column to datetime
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        print(df['date'].dtype)

        # Drop rows where date conversion failed (NaT values)
        if df['date'].isnull().any():
            print("Warning: Some dates could not be converted and are set as NaT (Not a Time). These rows will be removed.")
            print(df[df['date'].isnull()])
            df = df.dropna(subset=['date'])

        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except pd.errors.ParserError:
        raise ValueError(f"Parsing error while reading the file: {file_path}")

def analyze_publication_dates(df):
    """
    Analyze the frequency of news publications by month.
    """
    try:
        # Aggregate the number of publications by month
        date_trends = df['date'].dt.to_period('M').value_counts().sort_index()
        return date_trends
    except Exception as e:
        print(f"Error in analyzing publication dates: {e}")
        return None

def plot_publication_trends(date_trends):
    """
    Plot the number of publications over time to observe trends.
    """
    try:
        plt.figure(figsize=(12, 6))
        date_trends.plot(kind='line', marker='o', color='b')
        plt.title('Number of Publications Over Time')
        plt.xlabel('Month')
        plt.ylabel('Number of Publications')
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"Error in plotting publication trends: {e}")

def analyze_publishers(df):
    """
    Analyze the distribution of news articles by publisher.
    """
    try:
        # Get the count of publications per publisher
        publisher_counts = df['publisher'].value_counts()
        return publisher_counts
    except Exception as e:
        print(f"Error in analyzing publishers: {e}")
        return None

def plot_publisher_distribution(publisher_counts):
    """
    Plot the distribution of publications by publisher.
    """
    try:
        plt.figure(figsize=(10, 6))
        sns.barplot(x=publisher_counts.values, y=publisher_counts.index, palette='viridis')
        plt.title('Number of Publications by Publisher')
        plt.xlabel('Number of Publications')
        plt.ylabel('Publisher')
        plt.show()
    except Exception as e:
        print(f"Error in plotting publisher distribution: {e}")
