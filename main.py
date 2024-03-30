import streamlit as st
import requests
from datetime import date

today = date.today().strftime("%B %d, %Y")

api_key = "bn3TQDOfi9hNsm4xBU52dFtOXO7XiLb9B2IqD82s"
url = f"https://api.nasa.gov/planetary/apod?&api_key={api_key}"

request = requests.get(url)
content = request.json()

st.title(today)
st.title(content["title"])
st.image(content["url"])
st.write(content["explanation"])
