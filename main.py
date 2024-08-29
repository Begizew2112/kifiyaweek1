import preprocess
import sentiment_analysis
import time_series_analysis
import publisher_analysis

def main():
    # Step 1: Preprocess data
    df = preprocess.load_and_preprocess_data('../data/raw_analyst_ratings.csv')
    
    # Step 2: Sentiment Analysis
    df = sentiment_analysis.perform_sentiment_analysis(df)
    
    # Step 3: Time Series Analysis
    time_series_analysis.analyze_publication_dates(df)
    time_series_analysis.analyze_publication_times(df)
    
    # Step 4: Publisher Analysis
    publisher_analysis.analyze_publishers(df)
    publisher_analysis.analyze_domains(df)

if __name__ == "__main__":
    main()
