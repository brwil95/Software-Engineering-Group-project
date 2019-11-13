import requests
import json

class Queue:
    def __init__(self):
        self.queue = []

    def add_stored(self, stored):
        self.queue.insert(0, stored)


    def remove_stored(self):
        return self.queue.pop()

    def get_stored(self):
        return self.queue[0]

    def get_value(self):
        return self.queue[0]

    def empty_queue(self):
        for item in self.queue:
            self.queue.pop()
        return

    def not_empty(self):
        if len(self.queue) == 0:
            return False
        else:
            return True

    def queue_length(self):
        return len(self.queue)

def api(q, health_type, health, diet, calories):
    values = {'health_type': health_type,
              'healt': health,
              'diet': diet,
              'calories': calories}
    url = 'https://api.edamam.com/search?q=' + q.lower()
#     if(health == ''):
#         url += '&health_type=' + health_type.lower() + '&diet=' + diet.lower() + '&calories=0-' + calories + '&app_id=5ef19f8a&app_key' \
#                 '=4a892acba31294ff42ec114868b7ffce '
    for item in values:
        if values[item] != '':
            if item == 'calories':
                url += '&' + item + '=0-' + values[item]
            else:
                url += '&'+ item + '=' + values[item].lower()
    url += '&app_id=5ef19f8a&app_key=4a892acba31294ff42ec114868b7ffce '
    response = requests.get(url)
    return response.json()

def specific_recipe(q, health_type, health, diet, calories, recipe):
    values = {'health_type': health_type,
              'healt': health,
              'diet': diet,
              'calories': calories}

    url = 'https://api.edamam.com/search?q=' + q.lower() + '&label=' + recipe.lower()
    for item in values:
        if values[item] != '':
            if item == 'calories':
                url += '&' + item + '=0-' + values[item]
            else:
                url += '&'+ item + '=' + values[item].lower()
    url += '&app_id=5ef19f8a&app_key=4a892acba31294ff42ec114868b7ffce '

    response = requests.get(url)
    return response.json()

