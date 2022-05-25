import requests
from twilio.rest import Client

STOCK_KEY = "YBWOHJQMY5AA9YCM"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
account_sid = "AC426910d1753c731ce22fbce94ea492f2"
auth_token = "628874d36d177d7c3fd4ca158f6c22bf"


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "IBM",
    "apikey": STOCK_KEY
}

response = requests.get("https://www.alphavantage.co/query",params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for key, value in data.items()]
yesterday_data = data_list[0]
day_before_yesterday_data = data_list[1]
yesterday_closing_price = yesterday_data["4. close"]
day_before_closing_price = day_before_yesterday_data["4. close"]
difference = float(yesterday_closing_price) - float(day_before_closing_price)
diff_percent = round((difference / float(yesterday_closing_price)) * 100)
if abs(diff_percent) > 1:
    news_params = {
        "apiKey": "f1cf70a1453f4c6c9859567acb396bfe",
        "qInTitle": "IBM",
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    client = Client(account_sid, auth_token)
    account_sid = "AC426910d1753c731ce22fbce94ea492f2"
    auth_token = "628874d36d177d7c3fd4ca158f6c22bf"
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+16184081292",
            to="+91 70929 26557",
        )
        print(message.status)

