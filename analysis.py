from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from scraper import wsj

def SentimentAnalysis(news):
    news = news
    scores = news

    #Create Instance
    analyzer = SentimentIntensityAnalyzer()

    #Analysis
    for f, v in news.items():
        sentiment_dict = analyzer.polarity_scores(v)

        if sentiment_dict['compound'] >= 0.05 :
            scores.update({f:sentiment_dict['compound']})
        
        elif sentiment_dict['compound'] <= - 0.05 : 
            scores.update({f:sentiment_dict['compound']})
        
        else: 
            scores.update({f:sentiment_dict['compound']})
    
    return scores

def Result(scores):
    positive_count = 0
    negative_count = 0 
    neutral_count = 0
    result = None

    for f, v in scores.items():
        if v >= 0.05:
            positive_count += 1
        elif v <= -0.05:
            negative_count += 1
        else:
            neutral_count += 1

    #Get Final Result
    if positive_count > negative_count and positive_count > neutral_count:
        result = "POSITIVE"
    
    elif negative_count > positive_count and negative_count > neutral_count:
        result = "NEGATIVE"

    else: 
        result = "NEUTRAL"

    return result   