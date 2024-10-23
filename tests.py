import unittest
from weather_api import get_weather_data
from data_processor import process_weather_update
from data_processor import kelvin_to_celsius, calculate_daily_summary

class WeatherMonitorTests(unittest.TestCase):

    def test_kelvin_to_celsius(self):
        self.assertAlmostEqual(kelvin_to_celsius(300), 26.85, places=2)


    def test_weather_data_retrieval(self):
        weather = get_weather_data('Delhi')
        self.assertIsNotNone(weather)

    import data_processor 

def test_daily_summary(self):
    data_processor.weather_data['2024-10-23'] = [
        {'temp': 300, 'feels_like': 303, 'main': 'Clear'},
        {'temp': 298, 'feels_like': 300, 'main': 'Clear'},
        {'temp': 302, 'feels_like': 305, 'main': 'Clear'},
    ]

    avg_temp, max_temp, min_temp, dominant_condition = calculate_daily_summary('2024-10-23')

    self.assertEqual(dominant_condition, 'Clear')
    self.assertAlmostEqual(avg_temp, 26.85, places=2)
    self.assertEqual(max_temp, 28.85)
    self.assertEqual(min_temp, 25.85)


if __name__ == '__main__':
    unittest.main()