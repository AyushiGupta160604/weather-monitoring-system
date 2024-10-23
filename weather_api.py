import requests
import os

API_KEY = os.getenv('OPENWEATHER_API_KEY', '#Your_API_key') 

def get_weather_data(city_name):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status() 
        data = response.json()
        print(f"Weather data fetched for {city_name}: {data}")
        return {
            'main': data['weather'][0]['main'],
            'temp': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'dt': data['dt']
        }
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except Exception as err:
        print(f"Other error occurred: {err}")
        return None
