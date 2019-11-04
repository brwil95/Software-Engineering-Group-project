import requests
import json



def api(q, health_type, health, diet, calories):
    url = 'https://api.edamam.com/search?q=' + q.lower() +'&health_type=' + health_type.lower() +'&healt=' + health.lower() + '&diet=' + diet.lower() + '&calories=0-' + calories + '&app_id=5ef19f8a&app_key' \
          '=4a892acba31294ff42ec114868b7ffce '
    response = requests.get(url)
    return response.json()

def lunch():
    url ='https://api.edamam.com/search?q=lunch&health_type=vegan&app_id=5ef19f8a&app_key' \
          '=4a892acba31294ff42ec114868b7ffce '
    response = requests.get(url)
    return response.json()


def dinner():
    url ='https://api.edamam.com/search?q=dinner&health_type=vegan&app_id=5ef19f8a&app_key' \
          '=4a892acba31294ff42ec114868b7ffce '
    response = requests.get(url)

    return response.json()