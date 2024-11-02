# Simple Chatbot Project

## Description
This is a simple Python chatbot project that demonstrates object-oriented programming principles. The chatbot can respond to weather-related queries using a mock weather API and perform basic mathematical operations. Additionally, all conversations are logged to a file with timestamps.

## Project Structure
chatbot_project/
├── chatbot.py            # Core chatbot implementation
├── weather_api.py        # Mock weather API
├── tests/
│   └── test_chatbot.py   # Unit tests
├── conversation.log      # Log file for conversations
├── README.md             # Setup instructions
└── app.py                # Optional REST API (bonus challenge)

## Setup Instructions

### 1. Clone the repository
    git clone <your_repository_url> cd chatbot_project


### 2. Run the Chatbot
    python chatbot.py


### 3. Run Unit Tests
    python -m unittest discover tests


## Features
    - **User Interaction**: Greets the user, prompts for their name, and allows the user to query weather or perform math operations.
    - **Weather Queries**: Uses a mock API to simulate weather information retrieval by city.
    - **Math Operations**: Supports addition, subtraction, multiplication, and division with error handling.
    - **Conversation Logging**: Logs all user interactions to `conversation.log`.

## Optional REST API
    The chatbot can also be run as a REST API using Flask.

### Start the REST API
    python app.py
    The API will be available at `http://127.0.0.1:5000`.

