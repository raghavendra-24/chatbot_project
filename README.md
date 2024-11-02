
# Chatbot Project

A simple Python-based chatbot that interacts with users by greeting them, providing real-time weather information for any specified city, and performing basic math operations.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Features

- **User Greeting**: Greets the user and requests their name for a personalized experience.
- **Weather Query**: Provides real-time weather data for cities using a weather API.
- **Math Operations**: Performs basic math calculations (addition, subtraction, multiplication, and division).
- **Logging**: Logs all interactions in `conversation.log` to maintain a record of user conversations.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/raghavendra-24/chatbot_project.git
   cd chatbot_project
   ```

2. **Install Requirements**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configuration**

The `WEATHER_API_KEY` environment variable is required for live weather data. Set it according to your operating system:

### For Windows

1. **Temporary (PowerShell)**: 
   ```powershell
   $env:WEATHER_API_KEY = "66c02b74f5020224d5fcec50c437057b"
   ```

2. **Temporary (Command Prompt)**:
   ```cmd
   set WEATHER_API_KEY=66c02b74f5020224d5fcec50c437057b
   ```

3. **Permanent**:
   - Open **Environment Variables** settings in Windows.
   - Under **User variables**, click **New**.
   - Set `WEATHER_API_KEY` as the **Variable name** and `66c02b74f5020224d5fcec50c437057b` as the **Variable value**.
   - Click **OK** to save.

### For macOS/Linux

Set the environment variable using `export` in the terminal:
```bash
export WEATHER_API_KEY="66c02b74f5020224d5fcec50c437057b"
```
## Configuration

The `WEATHER_API_KEY` environment variable is required for live weather data. You can store this in your terminal session or add it to your system's environment variables for persistence.

## Usage

To start the chatbot:
```bash
python chatbot.py
```

When running, the chatbot will prompt you with options to:
1. Check the weather
2. Perform a math operation
3. Exit

### Example Interaction

```plaintext
Hello! I'm your assistant chatbot.
What's your name? John
Nice to meet you, John!

Options:
1. Check the weather
2. Perform a math operation
3. Exit
Choose an option (1-3): 1
Please enter the city name: New York
The current weather in New York is Cloudy, 22°C
```

## Project Structure

- `chatbot.py`: Main script to run the chatbot and handle user interactions.
- `weather_api.py`: Contains the `WeatherAPI` class for live weather data.
- `conversation.log`: Logs interactions and user messages.
- `requirements.txt`: Lists the Python dependencies required for the project.

## Dependencies

- `requests`: For making HTTP requests to the weather service.

To install dependencies:
```bash
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Make changes and commit them:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Create a Pull Request.

## License

This project is open-source and available under the [MIT License](LICENSE).
