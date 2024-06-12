import functions
import FreeSimpleGUI as sg

label = sg.Text("Add a todo item: ")
inputBox = sg.InputText(tooltip="Enter todo", key="todo")
addButton = sg.Button("Add")
listBox = sg.Listbox(values=functions.getTodos(), key="todos",
                     enable_events=True, size=[45, 15])
editButton = sg.Button("Edit")
layout = [[label], [inputBox, addButton], [listBox, editButton]]
window = sg.Window('My To-Do App',
                   layout=layout,
                   font=('Helvetica', 20))
while True:
    event, values = window.read()
    print('event',event)
    print('values',values)
    match event:
        case 'Add':
            todos = functions.getTodos()
            newTodo = values['todo'] + '\n'
            todos.append(newTodo.title())
            functions.writeTodos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            todoEdit = values['todos'][0]
            newTodo = values['todo']
            todos = functions.getTodos()
            index = todos.index(todoEdit)
            todos[index] = newTodo + '\n'
            functions.writeTodos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            itemSelected = values['todos'][0].strip('\n')
            window['todo'].update(value=itemSelected)
        case sg.WINDOW_CLOSED:
            break

print('Bye!!')
window.close()

