import requests
import json
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
print(response.status_code)
#create a formatted string of the Python JSON object
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())