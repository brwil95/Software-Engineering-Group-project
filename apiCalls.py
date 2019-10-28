import requests
import json


# todo will eventually take in data
def api():
    url = 'https://api.edamam.com/search?q=cookies&health_type=vegan&app_id=5ef19f8a&app_key' \
          '=4a892acba31294ff42ec114868b7ffce '
    response = requests.get(url)
    return response.json()