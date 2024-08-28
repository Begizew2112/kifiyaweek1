# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import os


# class FinancialNewsEDA:
#     def __init__(self, file_path):
#         """
#         Initialize the FinancialNewsEDA class with a file path.
#         """
#         self.file_path = file_path
#         self.df = self.load_data()

#     def load_data(self):
#         """
#         Load data from a CSV file and handle potential issues with data loading.
#         """
#         try:
#             # Load data from CSV
#             df = pd.read_csv(self.file_path)
#             print("Data loaded successfully.")
#             print(df.dtypes)
#             print(df.head())
            
#             # Convert 'date' column to datetime
#             df['date'] = pd.to_datetime(df['date'], errors='coerce')
#             print(df['date'].dtype)

#             # Drop rows where date conversion failed (NaT values)
#             if df['date'].isnull().any():
#                 print("Warning: Some dates could not be converted and are set as NaT (Not a Time). These rows will be removed.")
#                 print(df[df['date'].isnull()])
#                 df = df.dropna(subset=['date'])

#             return df
#         except FileNotFoundError:
#             raise FileNotFoundError(f"File not found: {self.file_path}")
#         except pd.errors.ParserError:
#             raise ValueError(f"Parsing error while reading the file: {self.file_path}")

#     def analyze_publication_dates(self):
#         """
#         Analyze the frequency of news publications by month.
#         """
#         try:
#             # Aggregate the number of publications by month
#             date_trends = self.df['date'].dt.to_period('M').value_counts().sort_index()
#             return date_trends
#         except Exception as e:
#             print(f"Error in analyzing publication dates: {e}")
#             return None

#     def plot_publication_trends(self, date_trends):
#         """
#         Plot the number of publications over time to observe trends.
#         """
#         try:
#             plt.figure(figsize=(12, 6))
#             date_trends.plot(kind='line', marker='o', color='b')
#             plt.title('Number of Publications Over Time')
#             plt.xlabel('Month')
#             plt.ylabel('Number of Publications')
#             plt.grid(True)
#             plt.show()
#         except Exception as e:
#             print(f"Error in plotting publication trends: {e}")

#     def analyze_publishers(self):
#         """
#         Analyze the distribution of news articles by publisher.
#         """
#         try:
#             # Get the count of publications per publisher
#             publisher_counts = self.df['publisher'].value_counts()
#             return publisher_counts
#         except Exception as e:
#             print(f"Error in analyzing publishers: {e}")
#             return None

#     def plot_publisher_distribution(self, publisher_counts):
#         """
#         Plot the distribution of publications by publisher.
#         """
#         try:
#             plt.figure(figsize=(10, 6))
#             sns.barplot(x=publisher_counts.values, y=publisher_counts.index, palette='viridis')
#             plt.title('Number of Publications by Publisher')
#             plt.xlabel('Number of Publications')
#             plt.ylabel('Publisher')
#             plt.show()
#         except Exception as e:
#             print(f"Error in plotting publisher distribution: {e}")


# # Main execution
# if __name__ == "__main__":
#     # Construct the path to the data file
#     script_dir = os.path.dirname(__file__)
#     relative_path = "../data/raw_analyst_ratings.csv"
#     file_path = os.path.join(script_dir, relative_path)

#     # Create an instance of FinancialNewsEDA
#     eda = FinancialNewsEDA(file_path)

#     # Perform publication date analysis
#     publication_date_trends = eda.analyze_publication_dates()
#     if publication_date_trends is not None:
#         print(publication_date_trends)
#         eda.plot_publication_trends(publication_date_trends)

#     # Perform publisher analysis
#     publisher_counts = eda.analyze_publishers()
#     if publisher_counts is not None:
#         print(publisher_counts)
#         eda.plot_publisher_distribution(publisher_counts)
