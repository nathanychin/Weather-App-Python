from flask import Flask, jsonify

import requests
import json

app = Flask(__name__)

@app.route('/weather/alerts')
def get_weather_alerts():
    response = requests.get('https://api.weather.gov/alerts/active?&status=actual').json()
    alerts = []
    for x in response['features']:
        alert = {
            'areaDesc': x['properties']['areaDesc'],
            'status': x['properties']['status'],
            'messageType': x['properties']['messageType'],
            'headline': x['properties']['headline'],
            'severity': x['properties']['severity']
        }
        alerts.append(alert)
    return jsonify(alerts)

if __name__ == '__main__':
    app.run(debug=True)