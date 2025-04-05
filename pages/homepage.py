import streamlit as st
import streamlit.components.v1 as components
import requests

st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Home</title>
<style type="text/css">
@import url("homepage.css");
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

components.html(html_content, scrolling=True)