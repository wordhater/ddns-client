# PYTHON NAMECHEAP DDNS CLIENT - DOCKER

## Purpose

At least for namecheap, there is a lack of linux support for their DDNS. This was created to work around this issue

## Setup

[Install Docker Engine](https://docs.docker.com/engine/install/)

[Install docker-compose](https://docs.docker.com/compose/install/#scenario-two-install-the-compose-plugin)

Create a file named config.json if it doesn't already exist, and fill out with the content below

leave ip address blank for automatic selection of ip

### example contents

```json
{
    "domain": "example.com",
    "password": "long string of numbers/letters",
    "ip": "",
    "host": ["www", "@"],
    "delay": 600
}
```

## To-Do

- move config options to docker-compose.yaml