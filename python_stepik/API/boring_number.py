import requests
import json

with open("dataset_24476_3.txt") as file:
    for number in file:
        number = number.strip()
        params = {
            'default': "boring",
            'json': True
        }
        api_url = "http://numbersapi.com/{}/math".format(number)
        res = requests.get(api_url, params=params).text
        data = json.loads(res)
        if 'boring' in data['text']:
            print("Boring")
        else:
            print("Interesting")

