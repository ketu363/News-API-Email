# This project is just for demo how to send image via api to run this you need to run "streamlit run NasaDemo.py" in terminal
import requests
import streamlit as st


# Prepare API key and url
api_key1 = "JPFfz2StMF5wSFf5R6V5rklZmkaCDq3tWTeoc4i6"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key1}"

# Get the request data as a dictionary
response1 = requests.get(url)
data = response1.json()

# Extract the Image tittle, url and, explanation
title1 = "Welcome to Nishant'/s NASA Page"
title2 = data["title"]
image_url = data["url"]
explanation = data["explanation"]

# Download the image
image_filepath = "img.png"
response2 = requests.get(image_url)
with open(image_filepath, "wb") as file:
    file.write(response2.content)

st.title(title1)
st.title(title2)
st.image(image_filepath)
st.write(explanation)


