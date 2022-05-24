import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
url = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "74a2280a8e68531266636cbbd76dc620"

weather_params = {
            "lat": 13.248624522117854,
            "lon": 80.15706313086551,
            "exclude": "current,minutely,daily,alerts",
            "appid": api_key,
}

rain_came = False

response = requests.get(url, params=weather_params)
response.raise_for_status()
data = response.json()
data_slice = data["hourly"][:12]
for each in data_slice:
    # print(each["hourly"][0]["weather"][0]["id"])
    condition = int(each["weather"][0]["id"])
    if condition < 600:
        rain_came = True

if rain_came:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="YOUR TWILIO VIRTUAL NUMBER",
        to="YOUR TWILIO VERIFIED REAL NUMBER"
    )
    print(message.status)