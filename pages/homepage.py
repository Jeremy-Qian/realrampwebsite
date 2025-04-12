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
col1, col2 = st.columns([0.70, 0.24])

with col1:
    st.markdown("### Trending")
    
    
    colcard1, colcard2, colcard3 = st.columns([0.33, 0.33, 0.33])
    with colcard1:
        card(
            title="Bookshop",
            text="Explore our bookshop and find the perfect books for your reading needs.",
            url="bookshop",
            styles={
                "card": {
                    "border-radius": "15px",
                    "width": "100%",  # 修改为100%填满列宽
                    "padding": "5px",
                    "margin": "0px",  # 移除外边距
                    "height": "170px",
                    "background-color": "rgba(255, 0, 25, 0.5)",
                },
                "title": {"font-size": "24px", "font-weight": "bold"},
                "text": {"font-size": "16px"}
            }
        )
    with colcard2:
        card(
            title="Ramp Day",
            text="The date of National Ramp Day is being figured out-- Click here to find out more...",
            styles={
                "card": {
                    "border-radius": "15px",
                    "width": "100%",
                    "padding": "5px",
                    "margin": "0",
                    "height": "170px",
                    "background-color": "rgba(0, 187, 255, 0.5)",
                },
                "title": {"font-size": "24px", "font-weight": "bold"},
                "text": {"font-size": "16px"}
            }
        )
    with colcard3:
        card(
            title="Time Chart (beta)",
            text="Click here for the new ramp time chart!",
            styles={
                "card": {
                    "border-radius": "15px",
                    "width": "100%",
                    "padding": "5px",
                    "margin": "0",
                    "height": "170px",
                    "background-color": "rgba(255, 200, 0, 0.5)",
                },
                "title": {"font-size": "24px", "font-weight": "bold"},
                "text": {"font-size": "16px"}
            }
        )
    st.markdown("""
    <style>
    div[data-testid="stColumn"] {
        background-color: #FFFFEC;
        
        border-radius: 5px;
        padding: 0px;
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
