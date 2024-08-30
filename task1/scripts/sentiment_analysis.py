import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

def perform_sentiment_analysis(df):
    # Initialize Sentiment Intensity Analyzer
    sia = SentimentIntensityAnalyzer()
    
    # Perform sentiment analysis
    df['sentiment_score'] = df['headline'].apply(lambda x: sia.polarity_scores(x)['compound'])
    df['sentiment_category'] = df['sentiment_score'].apply(lambda x: 'very_negative' if x < -1 else ('negative' if x < -0.05 else ('positive' if x > 0.05 else 'neutral')))
    
    # Save the results
    df.to_csv('sentiment_analysis_results.csv', index=False)
    return df
