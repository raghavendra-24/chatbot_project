import datetime
import random
from weather_api import MockWeatherAPI

class Chatbot:
    def __init__(self, name="Chatbot"):
        # Initialize chatbot with a default name and logging file
        self.name = name
        self.user_name = None
        self.weather_api = MockWeatherAPI()
        self.log_file = "conversation.log"
        self.log_conversation(f"Chatbot '{self.name}' started.")

    def log_conversation(self, message):
        # Logs a message to the conversation log with a timestamp
        with open(self.log_file, "a") as log:
            log.write(f"{datetime.datetime.now()} - {message}\n")

    def greet_user(self):
        # Greet the user and ask for their name
        print("Hello! I'm your assistant chatbot.")
        self.user_name = input("What’s your name? ")
        self.log_conversation(f"User name: {self.user_name}")
        print(f"Nice to meet you, {self.user_name}!")

    def handle_weather_query(self):
        # Handles weather queries using the mock API
        city = input("Please enter the city name: ")
        weather_info = self.weather_api.get_weather(city)
        if weather_info:
            print(f"The current weather in {city} is {weather_info}")
            self.log_conversation(f"Weather query for {city}: {weather_info}")
        else:
            print("Sorry, I couldn’t find the weather for that city.")
            self.log_conversation(f"Unknown city for weather query: {city}")

    def handle_math_operations(self, operation=None, num1=None, num2=None):
        if operation is None or num1 is None or num2 is None:
            # Interactive mode for user input
            try:
                operation = input("Choose an operation (add, subtract, multiply, divide): ").strip().lower()
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input. Please enter numerical values.")
                self.log_conversation("Invalid input for math operation.")
                return "Error"

        # Processing the math operation
        try:
            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 == 0:
                    print("Error: Cannot divide by zero!")
                    return "Error"
                result = num1 / num2
            else:
                print("Invalid operation!")
                return "Invalid operation"
            
            print(f"The result is: {result}")
            self.log_conversation(f"Math operation '{operation}' on {num1} and {num2}: {result}")
            return result  # Return the result for test verification
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return "Error"

    def start(self):
        # Start the chatbot interaction loop
        self.greet_user()
        while True:
            print("\nOptions:")
            print("1. Check the weather")
            print("2. Perform a math operation")
            print("3. Exit")
            choice = input("Choose an option (1-3): ")
            if choice == "1":
                self.handle_weather_query()
            elif choice == "2":
                self.handle_math_operations()
            elif choice == "3":
                print("Goodbye!")
                self.log_conversation("User exited the conversation.")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.start()
