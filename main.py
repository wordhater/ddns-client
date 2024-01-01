import json
import requests
from time import sleep
#load config.json

with open('config.json') as json_data:
    config = json.load(json_data)
autoip = False

print(config)
if config["ip"] == "":
    autoip = True
else:
    ip = config["ip"]
    autoip = False
print(autoip)

# main loop
while True:
    if autoip:
        ip = requests.get('https://api.ipify.org').content.decode('utf8')
    url = f"https://dynamicdns.park-your-domain.com/update?host={config["host"]}&domain={config["domain"]}&password={config["password"]}&ip={ip}"
    response = requests.get(url)
    sleep(360)