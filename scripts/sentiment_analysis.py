# scripts/sentiment_analysis.py
import pandas as pd
from textblob import TextBlob

def analyze_sentiment(df, text_column):
    """Perform sentiment analysis on the specified text column."""
    df['polarity'] = df[text_column].apply(lambda x: TextBlob(x).sentiment.polarity)
    df['subjectivity'] = df[text_column].apply(lambda x: TextBlob(x).sentiment.subjectivity)
    
    # Assign sentiment based on polarity score
    df['sentiment'] = df['polarity'].apply(lambda x: 'positive' if x > 0 else ('negative' if x < 0 else 'neutral'))
    
    return df

if __name__ == "__main__":
    df = pd.read_csv('data/merged_data.csv')
    df = analyze_sentiment(df, 'headline')
    df.to_csv('data/news_with_sentiment.csv', index=False)
