import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Home</title>
<style type="text/css">
    #container {
        width: 100%;       /* 示例：限制容器宽度 */
        margin: 2px auto; /* 居中 */
        font-family: Segoe, "Segoe UI", "DejaVu Sans", "Trebuchet MS", Verdana, sans-serif;
    }
    #banner {
        border: 2px solid #000;
        width: 100%;      /* 继承父容器宽度 */
        height: 100%;    /* 固定高度（或使用其他单位） */
        text-align: center;
        border-radius: 5px;
        overflow: hidden; /* 隐藏超出部分 */
    }
    #banner img {
        width: 100%;     /* 宽度填满 #banner */
        height: 100%;     /* 高度填满 #banner */
        object-fit: cover; /* 保持比例并覆盖区域（可选） */
        border-radius: 5px;
        border: 2px solid #000;
    }
    #content{
        float: left;
        margin-top: 2px;
        background: linear-gradient(to bottom left, #ECFFFF, 15%, #ABFFEC, 70%, #FFFFEC);
        height: 300px;
        width: 74%;
        border-radius: 5px;
        border: 2px solid #000;
        text-align: center;
    }
    #links{
        margin-top: 2px;
        border-radius: 5px;
        background: linear-gradient(to bottom right, #FFFFEC, 15%, #ABFFEC, 70%, #FFFFEC);
        float: right;
        border: 2px solid #000;
        text-align: center;
        width: 24%;
        height: 300px;
    }
    .link{
        color: lightseagreen;
        font-weight: 4000;
    }
</style>
</head>
	
<body>
    <div id="container">
        Content for id "container" Goes Here
      <div id="banner">
		  	<a href="https://contactus.streamlit.app" target="new">
            	<img src="../banner.gif" alt="Banner Image">
		  	</a>
        </div>
	  <iframe id="content">Hello </iframe>
	  <aside id="links">
	    <h2>Links</h2>
		  <p>
	    <li class="link"><a class="link" href="https://ramper.streamlit.app" target="new">Login Page</a></li>
			  <br>
			  <li class="link"><a class="link" href="https://rampion.streamlit.app" target="new">Old Ramp Website</a></li>
			  <br>
			  <li class="link"><a class="link" href="https://contactus.streamlit.app" target="_self">Contact Us</a></li>
		  </p>
	  </aside>
		<div id="map">
			<h3>Ramp Map</h3>
			<img src="../banner.gif" alt="Banner Image">
		</div>
	</div>
</body>
</html>
"""

components.html(html_content)