import streamlit as st
from streamlit_card import card
from pathlib import Path
import base64


st.set_page_config(page_title="Home", page_icon="material/home", layout="wide", initial_sidebar_state="expanded")

# Get absolute path for the banner image
banner_path = Path(__file__).parent.parent / "banner.gif"
# Get absolute path for the map image
map_path = Path(__file__).parent.parent / "rampmap.jpg"

# 顶部横幅
try:
    file_ = open(banner_path, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    st.markdown(
        f"""
        <div style="width: 100%; margin: 0; padding: 0;">
            <img src="data:image/gif;base64,{data_url}" alt="Banner Image" style="width: 100%;">
        </div>
        """,
        unsafe_allow_html=True,
    )
except FileNotFoundError:
    st.error("Banner image not found at: " + str(banner_path))

st.markdown("""
<style>
    .stToolbarActionButton {
        visibility: hidden;
    }
</style>
""", unsafe_allow_html=True)
# 主内容区域
col1, col2 = st.columns([0.74, 0.24])

with col1:
    with st.container():
        st.markdown("### Trending")
        card(
            title="Bookshop",
            text="Explore our bookshop and find the perfect books for your reading needs.",
            styles={
                "card": {
                    "border": "2px solid #000",
                    "border-radius": "5px",
                    "padding": "20px",
                    "height": "300px!important",
                    "background-color": "#FFFFEC",
                },
                "title": {"font-size": "24px", "font-weight": "bold"},
                "text": {"font-size": "16px"},
            }
        )
        st.markdown("""
        <style>
        div[data-testid="stColumn"] {
            background-color: #FFFFEC;
            border: 2px solid #000;
            border-radius: 5px;
            padding: 20px;
            height: 300px !important;
        }
        </style>
        """, unsafe_allow_html=True)

with col2:
    with st.container():
        st.markdown("### Links")
        st.markdown("[Login Page](https://ramper.streamlit.app)")
        st.markdown("[Old Ramp Website](https://rampion.streamlit.app)")
        st.markdown("[Contact Us](https://contactus.streamlit.app)")
        st.markdown("""
        <style>
        div[data-testid="stAppViewContainer"] {
            background-color: #FFFFEC;
            padding: 20px;
        }
        div[data-testid="stHeader"]  {
            background-color: #FFFFEC;
            border: 2px solid #000
            padding: 20px;
        }
        section[data-testid="stSidebar"]  {
            background-color: #FFFFEC;
            border: 2px solid #000;
            border-radius: 5px;
            padding: 20px;
        }
        </style>
        """, unsafe_allow_html=True)
# 地图区域
with st.container():
    st.markdown("### Ramp Map")
    st.image(map_path)
