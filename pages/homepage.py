import streamlit as st
import streamlit.components.v1 as components
import requests

st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

# 从GitHub获取HTML内容
github_url = "https://raw.githubusercontent.com/Jeremy-Qian/realrampwebsite/main/pages/homepage.html"
response = requests.get(github_url)
html_content = response.text

components.html(html_content, scrolling=True)