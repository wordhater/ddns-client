# PYTHON NAMECHEAP DDNS CLIENT

Check out the [docker branch](https://github.com/wordhater/ddns-client/tree/docker) for a docker version of this script

## Purpose

At least for namecheap, there is a lack of linux support for their DDNS. This was created to work around this issue

## Setup

Create a file named config.json in the path where your running the python script

leave ip address blank for automatic selection of ip

### example contents

```json
{
    "domain": "example.com",
    "password": "long string of numbers/letters",
    "ip": "0.0.0.0",
    "host": ["www", "@"],
    "delay": 600
}
```
Then run the setupenv.sh file to create and setup the virtual environment

run.sh will open the env and start the script
