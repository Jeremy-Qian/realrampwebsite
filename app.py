import streamlit as st

pages = {
    "Account": [
        st.Page("https://ramper.streamlit.app", title="Log Out"),
    ],
    "Resources": [
        st.Page("pages/homepage.py", title="Home"),
    ],
}

pg = st.navigation(pages)
pg.run()