import unittest
from chatbot import Chatbot

class TestChatbot(unittest.TestCase):
    def setUp(self):
        self.chatbot = Chatbot()

    def test_weather_query(self):
        # Test that the weather response is non-empty for valid inputs
        weather = self.chatbot.weather_api.get_weather("London")
        self.assertTrue(weather is not None)

    def test_math_operations(self):
        # Test addition functionality
        self.assertEqual(self.chatbot.handle_math_operations("add", 10, 5), 15)
        # Test division by zero handling
        self.assertEqual(self.chatbot.handle_math_operations("divide", 10, 0), "Error")

if __name__ == '__main__':
    unittest.main()
