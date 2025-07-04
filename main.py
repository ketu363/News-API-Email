import requests
from send_email import send_email

api_key = "ff490ab3ef9140059f1ecb81fac95543"

url = "https://newsapi.org/v2/everything?q=tesla&from=2025-06-04&sortBy=pub" \
        "lishedAt&apiKey=ff490ab3ef9140059f1ecb81fac95543"

# Make Request
request  = requests.get(url)

# Get a dictionary with data
content = request.json()

#Acess the article title and description
body = ""
for article in content["articles"]:
        if article["title"] is not None:
          body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)