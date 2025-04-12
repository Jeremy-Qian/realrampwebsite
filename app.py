import streamlit as st

pages = {
    "Home": [
        st.Page("pages/homepage.py", title="Home", icon=":material/home:"),
    ],
    "Shop": [
        st.Page("pages/bookshop.py", title="Bookshop", icon=":material/book:"),
    ]
}

pg = st.navigation(pages)
pg.run()
