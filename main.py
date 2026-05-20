from flask import Flask, request, jsonify
from flask_cors import CORS

from itinerary import generate_itinerary
from budget import allocate_budget

app = Flask(__name__)

CORS(app)


@app.route("/")
def home():

    return jsonify({
        "message": "Travel AI Running"
    })


@app.route("/generate-trip", methods=["POST"])
def generate_trip():

    data = request.json

    destination = data["destination"]

    days = int(data["days"])

    budget = float(data["budget"])

    vibe = data["vibe"]

    season = data["season"]

    itinerary = generate_itinerary(
        destination,
        days,
        budget,
        vibe,
        season
    )

    budget_data = allocate_budget(budget)

    return jsonify({

        "itinerary": itinerary,

        "budget": budget_data

    })


if __name__ == "__main__":

    app.run(debug=True)