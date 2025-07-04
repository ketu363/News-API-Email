import requests
from send_email import send_email

# Make the news topic variable
topic ="tesla"

api_key = "ff490ab3ef9140059f1ecb81fac95543"

url = "https://newsapi.org/v2/everything?" \
       f"q={topic}&" \
       "from=2025-06-04&" \
       "sortBy=publishedAt&" \
       "apiKey=ff490ab3ef9140059f1ecb81fac95543&" \
       "language=en"


# Make Request
request  = requests.get(url)

# Get a dictionary with data
content = request.json()

#Acess the article title and description
body = "Subject: Today's Tesla News\n\n"
for article in content["articles"][:20]:
    title = article.get("title") or ""
    description = article.get("description") or ""
    url = article.get("url") or ""

    body = body + title + "\n" + description + "\n" + url + "\n\n"

body = body.encode("utf-8")
send_email(message=body)