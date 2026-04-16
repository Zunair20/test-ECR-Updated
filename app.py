import requests
from flask import Flask

app = Flask(__name__)

@app.route('/proxy')
def proxy_request():
    # Use 'requests' library to call an external API
    response = requests.get('https://educative.io')
    return response.json()
