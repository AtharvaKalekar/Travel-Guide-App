from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Sample travel destinations
destinations = ["Paris", "Tokyo", "New York", "London", "Rome", "Sydney", "Dubai"]

@app.route('/')
def home():
    return "Welcome to the Travel Guide!"

# Endpoint to generate an itinerary
@app.route('/generate-itinerary', methods=['POST'])
def generate_itinerary():
    data = request.json
    num_days = data.get('num_days', 3)  # Default to 3 days

    itinerary = []
    for _ in range(num_days):
        destination = random.choice(destinations)
        itinerary.append(destination)

    return jsonify({"itinerary": itinerary})

if __name__ == '__main__':
    app.run(debug=True)
