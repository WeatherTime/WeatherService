from flask import Flask, request, jsonify, make_response
import sys
sys.path.append('Classes')
sys.path.append('WebScraping')
import weatherScraping
import var

app = Flask(__name__)

@app.route("/get-weather")
def get_weather():
    weather = weatherScraping.get_weather(var.location)

    # Generate response data
    data = weather.weather_to_dict()
    resp = make_response(jsonify(data))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp, 200    

if __name__ == "__main__":
    # Run the app
    app.run(debug=False)