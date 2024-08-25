import streamlit as st
# print(dir(st))

from pathlib import Path
import base64
# from streamlit import *
# Set the app title

st.set_page_config(
     page_title='Streamlit-LEARNING',
     layout="wide",
     initial_sidebar_state="expanded",
)
st.title("Streamlit-LEARNING")

# Thanks to streamlitopedia for the following code snippet

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


CSS = """
    <style>
        # body {
        #     font-family: Arial, sans-serif;
        #     background-color: #F8F9FA;
        # }
        # h1 {
        #     font-size: 24px;
        #     text-align: center;
        #     margin-bottom: 10px;
        # }
        
    </style>
    """

st.markdown(CSS, unsafe_allow_html=True)

image_path = 'bg.jpg'
image_encoded = img_to_bytes(image_path)
st.markdown("""<img src='data:image/png;base64{image_encoded}""", unsafe_allow_html=True)


