import streamlit as st
from PIL import Image

with st.expander("Start Camera"):
    cameraImage = st.camera_input("Camera")

if cameraImage:
    img = Image.open(cameraImage)
    grayImage = img.convert("L")
    st.image(grayImage)