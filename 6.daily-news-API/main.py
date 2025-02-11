import requests
from sendEmail import sendEmail

url = "https://newsapi.org/v2/everything?q=tesla&from=2025-01-11&sortBy=publishedAt&apiKey=58fddba2e9a24b36bc899db833a0446b"

request = requests.get(url)
content = request.json()

articles = content["articles"]

body = ""
for article in articles:
    title = article["title"]
    description = article["description"]
    if description is not None and title is not None:
        body = body + title + "\n" + description + "\n" + "\n"

body = body.encode("utf-8")
print(body)
#sendEmail(body)
