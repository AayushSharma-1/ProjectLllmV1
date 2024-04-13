import streamlit as st
import requests
query = st.text_area('Enter the Query', height=200)
prompt = query
link = "https://potential-parakeet-w6jpp4vrxj25vgv-8000.app.github.dev/chat/" + prompt
request = requests.get(link)
st.write(request.json())