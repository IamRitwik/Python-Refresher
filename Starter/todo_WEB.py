import streamlit as st
import functions

todos = functions.getTodos()

st.title('My Todo App')
st.subheader('Write your todos:')

for todo in todos:
    st.checkbox(todo)

st.text_input(label='', placeholder='Add a todo')