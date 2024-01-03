# PYTHON NAMECHEAP DDNS CLIENT

## Purpose

At least for namecheap, there is a lack of linux support for their DDNS. This was created to work around this issue

## Config

Create a file named config.json in the path where your running the python script

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
