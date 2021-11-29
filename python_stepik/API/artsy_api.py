import requests
import json

client_id = '345df73faff8316a7a53'
client_secret = '2c95a0f77eafa2cecf8fe688ced2d916'

r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })
j = json.loads(r.text)

token = j["token"]

artist_list = []

with open("dataset_24476_4.txt") as file:
    for artist_id in file:
        artist_id = artist_id.strip()
        api_url = "https://api.artsy.net/api/artists/{}".format(artist_id)
        params = {"xapp_token": token}
        res = requests.get(api_url, params=params).text
        data = json.loads(res)
        artist_list.append({'name': data['sortable_name'], 'birthday': data['birthday']})

print(artist_list)

for artist in sorted(artist_list, key=lambda x: (x['birthday'], x['name'])):
    print(artist['name'])
