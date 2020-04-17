from analysis import SentimentAnalysis, Result
from scraper import wsj, yahoo_finance
import json

def get_company():
    company = input("Company: ")
    return company

def get_ticker():
    ticker = input("Ticker: ")
    return ticker

def get_news(company):
    news = wsj(company)
    return news

def get_scores(news):
    scores = SentimentAnalysis(news)
    return scores

def get_stocks(ticker):
    stocks = yahoo_finance(ticker)
    return stocks

#JSON
def get_news_json(news):
    news = json.dumps(news)
    return news

def get_scores_json(scores):
    scores = json.dumps
    return scores

def get_stocks_json(stocks):
    stocks = json.dumps
    return stocks

def news_json(company):
    news = get_news(company)
    news_json = get_news_json(news)
    return news