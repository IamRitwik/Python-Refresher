import streamlit as st
import functions

todos = functions.getTodos()


def addTodo():
    todo = st.session_state["todo"] + '\n'
    todos.append(todo)
    print(todos)
    functions.writeTodos(todos)


st.title('My Todo App')
st.subheader('Write your todos:')

for todo in todos:
    st.checkbox(todo)

st.text_input(label='', placeholder='Add a todo',
              on_change=addTodo, key="todo")

st.session_state