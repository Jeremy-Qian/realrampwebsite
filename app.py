import streamlit as st

pages = {
    "Resources": [
        st.Page("pages/homepage.py", title="Home"),
    ],
    "Shop": [
        st.Page("pages/bookshop.py", title="Bookshop"),
    ]
}

pg = st.navigation(pages)
pg.run()
