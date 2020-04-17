from lxml import html
import requests, time, json
from datetime import datetime, timedelta

def wsj(company):
    news = {}

    headlines = []
    dates = []

    today = datetime.today()
    delta = timedelta(days = 7)
    start_date = today - delta

    today = today.strftime("%Y/%m/%d")
    start_date = start_date.strftime("%Y/%m/%d")

    for i in range(1,6):
        link = 'https://www.wsj.com/search/term.html?KEYWORDS=' +company+ '&min-date=' +start_date+ '&max-date=' +today+ '&daysback=7d&isAdvanced=true&andor=AND&sort=relevance&source=wsjarticle,wsjblogs,wsjvideo,interactivemedia,sitesearch,wsjpro&page=' +str(i)+'.html'

        page = requests.get(link)
        tree = html.fromstring(page.content)
        headline = tree.xpath('//h3[@class="headline"]/a/text()')
        date = tree.xpath('//time[@class="date-stamp-container" or @class="date-stamp-container highlight"]/text()')

        for i in range(len(headline)):
            headlines.append(headline[i])
        for i in range(len(date)):
            dates.append(date[i])

    for i in range(len(headlines)):
        news.update({dates[i]: headlines[i]})
    
    return news

def yahoo_finance(ticker):
    stocks = {}

    dates = []
    data = []
    prices = []

    """
    !!! Yahoo Finance Uses Unix Time.
    """
    time2 = datetime.now()
    delta1 = timedelta(days = 7)
    time1 = time2 - delta1
    period2 = time2.strftime("%s")
    period1 = time1.strftime("%s")

    link ='https://finance.yahoo.com/quote/'+ticker+'/history?period1='+period1+'&period2='+period2+'&interval=1d&filter=history&frequency=1d.html'

    page = requests.get(link)
    tree = html.fromstring(page.content)
    dates = tree.xpath('//td[@class="Py(10px) Ta(start) Pend(10px)"]/span/text()')
    price = tree.xpath('//td[@class="Py(10px) Pstart(10px)"]/span/text()')

    for i in range(len(dates)):
        dates.append(dates[i])

    for i in range(len(price)):
        data.append(price[i])

    x = 3
    while x <= 27:
        prices.append(data[x])
        x += 6

    for i in range(len(prices)):
        stocks.update({dates[i]: prices[i]})
    
    return stocks