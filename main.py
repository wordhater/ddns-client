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
    for i in range(len(config["host"])):
        url = f"https://dynamicdns.park-your-domain.com/update?host={config["host"][i]}&domain={config["domain"]}&password={config["password"]}&ip={ip}"
        print(url)
        response = requests.get(url)
        sleep(20)
    sleep(config["delay"])