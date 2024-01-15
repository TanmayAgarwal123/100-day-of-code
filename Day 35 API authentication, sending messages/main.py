import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "8d370a2041d44f83713c29b1431171e3"

weather_params = {
    "lat": 25.192181,
    "lon": 75.850838,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
#print(response.json()["list"][0]["weather"][0]["id"])
will_rain = False
for hour_data in response.json()["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    print("Bring an umbrella")
else:
    print("No rain today")
    