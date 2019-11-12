import requests
import json

class Queue:
    def __init__(self):
        self.queue = []

    def add_stored(self, stored):
        self.queue.insert(0, stored)


    def remove_stored(self):
        return self.queue.pop()


def api(q, health_type, health, diet, calories):
    url = 'https://api.edamam.com/search?q=' + q.lower() +'&health_type=' + health_type.lower() +'&healt=' + health.lower() + '&diet=' + diet.lower() + '&calories=0-' + calories + '&app_id=5ef19f8a&app_key' \
          '=4a892acba31294ff42ec114868b7ffce '

    response = requests.get(url)
    return response.json()

def specific_recipe(q, health_type, health, diet, calories, recipe):
    url = 'https://api.edamam.com/search?q=' + q.lower() + '&label=' + recipe + '&health_type=' + health_type.lower() +'&healt=' + health.lower() + '&diet=' + diet.lower() + '&calories=0-' + calories + '&app_id=5ef19f8a&app_key' \
          '=4a892acba31294ff42ec114868b7ffce '

    response = requests.get(url)
    return response.json()

