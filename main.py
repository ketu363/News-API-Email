import requests

api_key = "ff490ab3ef9140059f1ecb81fac95543"

url = "https://newsapi.org/v2/everything?q=tesla&from=2025-06-04&sortBy=pub" \
        "lishedAt&apiKey=ff490ab3ef9140059f1ecb81fac95543"

# Make Request
request  = requests.get(url)

# Get a dictionary with data
content = request.json()

#Acess the article title and description
for article in content["articles"]:
        print(article["title"])
        print(article["description"])
