from collections import defaultdict
import time
from utils import kelvin_to_celsius

weather_data = defaultdict(list)

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin_temp):
    return (kelvin_temp - 273.15) * 9/5 + 32

def process_weather_update(city_name, weather):
    from alert_system import check_alerts
    celsius_temp = kelvin_to_celsius(weather['temp'])
    feels_like = kelvin_to_celsius(weather['feels_like'])
    
    date = time.strftime('%Y-%m-%d', time.gmtime(weather['dt']))
    weather_data[date].append({
        'temp': celsius_temp,
        'feels_like': feels_like,
        'main': weather['main']
    })

    print(f"Weather data for {city_name} on {date}: {weather_data[date]}")

# def calculate_daily_summary(date):
#     data_for_day = weather_data.get(date, [])
    
#     if len(data_for_day) == 0:
#         print(f"No data available for {date}")
#         return None, None, None, None

#     avg_temp = sum(d['temp'] for d in data_for_day) / len(data_for_day)
#     max_temp = max(d['temp'] for d in data_for_day)
#     min_temp = min(d['temp'] for d in data_for_day)

#     conditions = [d['main'] for d in data_for_day]
#     dominant_condition = max(set(conditions), key=conditions.count)

#     return avg_temp, max_temp, min_temp, dominant_condition

def calculate_daily_summary(date):
    avg_temp = sum([entry['temp'] for entry in weather_data[date]]) / len(weather_data[date])
    max_temp = max([entry['temp'] for entry in weather_data[date]])
    min_temp = min([entry['temp'] for entry in weather_data[date]])
    dominant_condition = max(set([entry['main'] for entry in weather_data[date]]), key=[entry['main'] for entry in weather_data[date]].count)
    
    print(f"Summary for {date}: Avg Temp={avg_temp}, Max Temp={max_temp}, Min Temp={min_temp}, Condition={dominant_condition}")  # Debugging line
    return avg_temp, max_temp, min_temp, dominant_condition