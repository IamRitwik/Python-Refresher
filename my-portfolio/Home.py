import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=400)

with col2:
    st.title("Ritwik Mukhopadhyay")
    content = """
    Hi!, I am Ritwik, I am a senior software engineer. I work in many different programming languages like Python,
    Java, JavaScript, TypeScript. I have developed many apps and services in Node JS, Spring Boot, React and Angular.
    Also I have knowledge in DevOps tools like Docker, Kubernetes and Azure Cloud platform.
    """

    st.info(content)

content_title = """
Below are some of the apps I have developed along with links to source code.
"""
st.write(content_title)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        title = row["title"]
        st.header(title)
        description = row["description"]
        st.write(description)
        thumbnail = "images/" + row["image"]
        st.image(thumbnail)
        st.write("[Source Code](https://github.com/IamRitwik/Python-Refresher.git)")

with col4:
    for index, row in df[10:].iterrows():
        title = row["title"]
        st.header(title)
        description = row["description"]
        st.write(description)
        thumbnail = "images/" + row["image"]
        st.image(thumbnail)
        st.write("[Source Code](https://github.com/IamRitwik/Python-Refresher.git)")
