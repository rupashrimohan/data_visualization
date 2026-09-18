import plotly.express as px
import json
import requests

# Make an API call and store the response
url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")
if r.status_code != 200:
    print(f"Failed to fetch data: {r.json().get('message', 'Unknown error')}")
    exit()
# Explore the structure of the data
response_dict = r.json()
response_string = json.dumps(response_dict, indent=4)
print(response_string)
