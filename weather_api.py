import requests

class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):
        # Call the OpenWeatherMap API to get the current weather for a city
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"  # To get the temperature in Celsius
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            weather_desc = data['weather'][0]['description']
            temperature = data['main']['temp']
            return f"{weather_desc.capitalize()}, {temperature}°C"
        else:
            return None
