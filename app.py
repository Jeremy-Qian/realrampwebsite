import streamlit as st

pages = {
    "Resources": [
        st.Page("pages/homepage.py", title="Home"),
    ],
}

pg = st.navigation(pages)
pg.run()