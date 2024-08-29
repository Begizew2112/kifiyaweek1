#import the neccessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_publication_dates(df):
    df['day_of_week'] = df['date'].dt.day_name()
    day_counts = df['day_of_week'].value_counts()
    
    # Plot the number of articles by day of the week
    plt.figure(figsize=(8, 5))
    sns.barplot(x=day_counts.index, y=day_counts.values, palette="muted")
    plt.title('Number of Articles by Day of the Week')
    plt.xlabel('Day of the Week')
    plt.ylabel('Number of Articles')
    plt.show()

def analyze_publication_times(df):
    df['hour'] = df['date'].dt.hour
    
    # Plot the number of articles by hour of the day
    plt.figure(figsize=(10, 5))
    sns.histplot(df['hour'], bins=24, kde=False, color='purple')
    plt.title('Number of Articles Published by Hour of the Day')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Number of Articles')
    plt.grid(True)
    plt.show()
