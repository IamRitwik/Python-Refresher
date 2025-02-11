import requests
from sendEmail import sendEmail

url = "https://newsapi.org/v2/everything?" \
      "q=tesla&" \
      "sortBy=publishedAt&" \
      "apiKey=58fddba2e9a24b36bc899db833a0446b&" \
      "language=en"

request = requests.get(url)
content = request.json()

articles = content["articles"]

# Access the article title and description
body = "Subject: Today's news" + "\n"
for article in content["articles"][:20]:
    if (article["description"] is not None) and (article["title"] is not None):
        body = body + article["title"] + "\n"\
               + article["description"] \
               + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")

sendEmail(message=body)
