from flask import Flask, request, jsonify 
from chatbot import Chatbot

app = Flask(__name__)
chatbot = Chatbot()

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to the Chatbot API! Use /greet, /weather, or /math."})

@app.route("/greet", methods=["GET"])
def greet():
    return jsonify({"message": "Hello! I am your assistant chatbot."})

@app.route("/weather", methods=["GET"])
def weather():
    city = request.args.get("city")
    weather_info = chatbot.weather_api.get_weather(city)
    if weather_info:
        return jsonify({"city": city, "weather": weather_info})
    else:
        return jsonify({"error": "City not found"}), 404

@app.route("/math", methods=["POST"])
def math_operations():
    data = request.get_json()
    operation = data.get("operation")
    num1 = data.get("num1")
    num2 = data.get("num2")
    try:
        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                return jsonify({"error": "Cannot divide by zero"}), 400
            result = num1 / num2
        else:
            return jsonify({"error": "Invalid operation"}), 400
        return jsonify({"result": result})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input"}), 400

if __name__ == "__main__":
    app.run(port=5000, debug=True)
