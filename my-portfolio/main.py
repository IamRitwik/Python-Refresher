import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Ritwik Mukhopadhyay")
    content = """
    Hi!, I am Ritwik, I am a senior software engineer. I work in many different programming languages like Python,
    Java, JavaScript, TypeScript. Also I have knowledge in DevOps tools like Docker, Kubernetes and Azure Cloud platform.
    """

    st.info(content)