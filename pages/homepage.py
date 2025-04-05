import streamlit as st
from pathlib import Path
import base64

st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

# Get absolute path for the banner image
banner_path = Path(__file__).parent.parent / "banner.gif"

# 顶部横幅
try:
    file_ = open(banner_path, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="Banner Image">',
        unsafe_allow_html=True,
    )
except FileNotFoundError:
    st.error("Banner image not found at: " + str(banner_path))

st.markdown("""
<style>
    .stToolbarActionButton {
        visibility: hidden;
    }
""")
# 主内容区域
col1, col2 = st.columns([0.74, 0.24])

with col1:
    # 内容区域
    with st.container():
        st.markdown("### Content")
        st.write("Hello")
        st.markdown("""
        <style>
        div[data-testid="stVerticalBlock"] {
            background-color: #ECFFFF;
            border: 2px solid #000;
            border-radius: 5px;
            padding: 20px;
            height: 300px;
        }
        </style>
        """, unsafe_allow_html=True)

with col2:
    # 链接区域
    with st.container():
        st.markdown("### Links")
        st.markdown("[Login Page](https://ramper.streamlit.app)")
        st.markdown("[Old Ramp Website](https://rampion.streamlit.app)")
        st.markdown("[Contact Us](https://contactus.streamlit.app)")
        st.markdown("""
        <style>
        div[data-testid="stVerticalBlock"] {
            background-color: #FFFFEC;
            border: 2px solid #000;
            border-radius: 5px;
            padding: 20px;
            height: 300px;
        }
        </style>
        """, unsafe_allow_html=True)

# 地图区域
with st.container():
    st.markdown("### Ramp Map")
    st.image("../banner.gif", width=300)