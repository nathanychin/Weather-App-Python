import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Get user's IP address
    ip_address = requests.get('http://api.ipify.org').text

    # Use ip-api.com to get location data
    geo_data = requests.get(f'http://ip-api.com/json/{ip_address}').json()

    city = geo_data['city']
    region = geo_data['regionName']
    location = f"{city}, {region}"

    # Get alerts for the user's location
    response = requests.get(f'https://api.weather.gov/alerts?point={geo_data["lat"]},{geo_data["lon"]}').json()
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
    return render_template('index.html', alerts=alerts, location=location)

if __name__ == '__main__':
    app.run(debug=True)