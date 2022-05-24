import requests
import json

with open('2022-05-21.json') as f:
    data = json.load(f)

sample = data[0]

resp = requests.post("http://localhost:5000/questgen", json={'json_payload': sample})

print(resp.text)
