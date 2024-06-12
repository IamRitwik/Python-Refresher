import functions
import FreeSimpleGUI as sg

label = sg.Text("Add a todo item: ")
inputBox = sg.InputText(tooltip="Enter todo", key="todo")
addButton = sg.Button("Add")

window = sg.Window('My To-Do App',
                   layout=[[label], [inputBox, addButton]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.getTodos()
            newTodo = values['todo'] + '\n'
            todos.append(newTodo.title())
            functions.writeTodos(todos)
        case sg.WINDOW_CLOSED:
            break

window.close()

