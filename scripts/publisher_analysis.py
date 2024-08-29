import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_publishers(df):
    publisher_counts = df['publisher'].value_counts()
    
    # Plot the number of articles per publisher
    plt.figure(figsize=(12, 6))
    sns.barplot(x=publisher_counts.index, y=publisher_counts.values, palette="viridis")
    plt.title('Number of Articles per Publisher')
    plt.xlabel('Publisher')
    plt.ylabel('Number of Articles')
    plt.xticks(rotation=90)
    plt.show()

def analyze_domains(df):
    df['domain'] = df['publisher'].apply(lambda x: x.split('@')[-1] if '@' in x else x)
    domain_counts = df['domain'].value_counts()
    
    # Plot the number of articles per domain
    plt.figure(figsize=(12, 6))
    sns.barplot(x=domain_counts.index, y=domain_counts.values, palette="viridis")
    plt.title('Number of Articles per Domain')
    plt.xlabel('Domain')
    plt.ylabel('Number of Articles')
    plt.xticks(rotation=90)
    plt.show()
# this is all about publisher analysis