
# Chatbot Project

This is a chatbot application that can handle weather queries and perform basic math operations.

## Features

- Get real-time weather information based on the city entered by the user.
- Perform basic math operations like addition, subtraction, multiplication, and division.

## Requirements

- Python 3.x
- `requests` library for making API calls

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/raghavendra-24/chatbot_project.git
   cd chatbot_project
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

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

## Usage

1. Run the chatbot:
   ```bash
   python chatbot.py
   ```

2. Follow the prompts to interact with the chatbot.

## License

This project is licensed under the MIT License.
