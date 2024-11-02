import random

class MockWeatherAPI:
    def get_weather(self, city):
        # Simulate a weather API with random weather data
        weather_data = {
            "Sunny": "Sunny, 25°C",
            "Rainy": "Rainy, 18°C",
            "Cloudy": "Cloudy, 22°C",
            "Stormy": "Stormy, 15°C"
        }
        return weather_data.get(random.choice(list(weather_data.keys())), None)
