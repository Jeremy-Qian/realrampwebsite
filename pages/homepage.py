import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")
with open("homepage.html", "r") as f:
    html_content = f.read()
components.html(html_content, scrolling=True)