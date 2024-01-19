import requests
from datetime import date
from datetime import timedelta

# Using python in telling yestarday date


# Get today's date
today = date.today()

# Get 2 days earlier
YESTERDAY = today - timedelta(days=1)


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "E43DMRX2ZE3OXE4Z"
NEWS_API_KEY = "7d7a994b04324d0cb68b5903beabf251"
stock_value = []

stock_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,

}

news_parameter = {
    "q": "tesla",
    "apiKey": NEWS_API_KEY,
    "language": "en"
}

stock_response = requests.get("https://www.alphavantage.co/query", params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()
day = 0
for key in stock_data["Time Series (Daily)"]:
    if day <= 1:
        stock_value.append(stock_data["Time Series (Daily)"][key])
        day += 1
    else:
        break

close_24_hours = float(stock_value[0]['4. close'])
close_48_hours = float(stock_value[1]['4. close'])
percentage_change = ((close_24_hours - close_48_hours) * 100)/close_24_hours

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

if percentage_change <= -5 or percentage_change >= 5:
    print("get news")
    print("no news")
    news_response = requests.get("https://newsapi.org/v2/everything", params=news_parameter)
    news_response.raise_for_status()
    news_data = news_response.json()
    news_info = news_data['articles']

newss_info = news_info[0:2]

for items in newss_info:
    print(f"Headline: {items['title']}")
    print(f"Brief: {items['description']}\n")


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

