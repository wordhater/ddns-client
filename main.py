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
# main loop
while True:
    if autoip:
        
#    url = f"https://dynamicdns.park-your-domain.com/update?host={config["host"]}&domain={config["domain"]}&password={config["password"]}&ip={ip}"
#    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
#    response = requests.get("",headers=headers)