import requests
from twilio.rest import Client

# SMS messages API Client
account_sid = ''
auth_token = ''
send_to = ''
text_message = ''


# Weather API client interface
API_KEY = ''
LON = -118.404678
LAT = 34.080292
API = f"https://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LON}&appid={API_KEY}"

weather_data = requests.get(API).json()
weather_information = weather_data['list']
amount_under_800 = 0
will_rain = False

for data in weather_information:
    if data['weather'][0]['id'] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+18334630475',
        body=text_message,
        to=send_to
    )
    print(message.status)