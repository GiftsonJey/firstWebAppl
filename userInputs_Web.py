import streamlit as st
from userInputsFn import readTodo, writeToDo


def getNewTodo():
    newItem = st.session_state["new_todo"] + "\n"
    print(newItem)
    todoList.append(newItem)
    writeToDo("todo_gui.txt",todoList)


st.title("ToDo List")
st.subheader("manage all items")


todoList = readTodo("todo_gui.txt")

for items in todoList:
    st.checkbox(items, key=items)

st.text_input(label="Enter new items to be added",placeholder="Type here",
              on_change=getNewTodo, key='new_todo')

st.session_state

