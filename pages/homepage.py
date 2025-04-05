import streamlit as st

st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

# 顶部横幅
st.image("../banner.gif", use_column_width=True)
st.markdown("[Contact Us](https://contactus.streamlit.app)")

# 主内容区域
col1, col2 = st.columns([0.74, 0.24])

with col1:
    # 内容区域
    with st.container():
        st.markdown("### Content Area")
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