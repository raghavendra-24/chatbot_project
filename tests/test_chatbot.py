from unittest.mock import patch
import unittest
from chatbot import Chatbot

class TestChatbot(unittest.TestCase):
    def setUp(self):
        self.chatbot = Chatbot()

    @patch("weather_api.WeatherAPI.get_weather")
    def test_weather_query(self, mock_get_weather):
        # Mock the weather API response
        mock_get_weather.return_value = "Clear sky, 20°C"
        
        # Now calling the method should return the mocked response
        weather = self.chatbot.weather_api.get_weather("London")
        
        # Test that the mocked response is as expected
        self.assertTrue(weather is not None)
        self.assertEqual(weather, "Clear sky, 20°C")

    def test_math_operations(self):
        # Test addition functionality
        self.assertEqual(self.chatbot.handle_math_operations("add", 10, 5), 15)
        # Test division by zero handling
        self.assertEqual(self.chatbot.handle_math_operations("divide", 10, 0), "Error")

if __name__ == '__main__':
    unittest.main()
