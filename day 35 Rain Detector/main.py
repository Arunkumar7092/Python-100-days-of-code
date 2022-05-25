import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
url = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "74a2280a8e68531266636cbbd76dc620"
account_sid = "AC426910d1753c731ce22fbce94ea492f2"
auth_token = "628874d36d177d7c3fd4ca158f6c22bf"


weather_params = {
            # "lat": 13.248624522117854,
            # "lon": 80.15706313086551,
            "lat": 26.592772,
            "lon": 104.839317,
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
        print("yes")

if rain_came:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="+16184081292",
        to="+91 70929 26557"
    )
    print(message.status)