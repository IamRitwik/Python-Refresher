import requests

api_key = "58fddba2e9a24b36bc899db833a0446b"

url = "https://newsapi.org/v2/"

request = requests.get(url)
content = request.json()

articles = content["articles"]

for article in articles:
    print(article["title"])
