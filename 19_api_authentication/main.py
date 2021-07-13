import os
import requests
from secret import WEATHER_KEY, TWILIO_SID, TWILIO_AUTH
from twilio.rest import Client

API_KEY = WEATHER_KEY
LAT = 38.907192
LON = -77.036873

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
weather_params = {
    "lat": LAT,
    "lon": LON,
    "exclude": "current,minutely,daily",
    "appid": API_KEY,
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data)

first_twelve = weather_data["hourly"][:12]
print(first_twelve)
print(len(first_twelve))

will_rain = False

for hour, weather in enumerate(first_twelve):
    condition_code = weather["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

print(will_rain)

if will_rain:
    client = Client(TWILIO_SID, TWILIO_AUTH)

    message = client.messages \
        .create(
        body="Its going to rain today, remember to bring an \u2602",
        from_='+14087097313',
        to='+13124150559'
    )

    print(message.status)