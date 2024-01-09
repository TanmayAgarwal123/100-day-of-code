import requests
MY_LAT = 25.218501
MY_LONG = 75.879103

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json")
response.raise_for_status()
print(response.json())
