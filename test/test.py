import requests
import json

# with open('2022-05-21.json') as f:
#     data = json.load(f)

# sender = data[0]['content'].replace('\n','').replace('\t',' ').strip()

resp = requests.post("http://localhost:5000/questgen", files={'file': "Joanna is a pretty woman and she is very happy."})

print(resp.text)