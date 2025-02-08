import functions
import FreeSimpleGUI as sg
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

sg.theme('Black')

label = sg.Text("Add a todo item: ")
inputBox = sg.InputText(tooltip="Enter todo", key="todo")
addButton = sg.Button(size=2, image_source="../files/add.png",
                      mouseover_colors="LightBlue", tooltip="Add a todo", key="Add")
listBox = sg.Listbox(values=functions.getTodos(), key="todos",
                     enable_events=True, size=[45, 15])
editButton = sg.Button("Edit")
completeButton = sg.Button(size=2, image_source="../files/complete.png",
                           mouseover_colors="LightBlue", tooltip="Complete a todo", key="Complete")
exitButton = sg.Button("Exit")

layout = [[label], [inputBox, addButton], [listBox, editButton, completeButton], [exitButton]]
window = sg.Window('My To-Do App',
                   layout=layout,
                   font=('Helvetica', 20))
while True:
    event, values = window.read()
    print('event', event)
    print('values', values)
    match event:
        case 'Add':
            todos = functions.getTodos()
            if values['todo'] != '':
                newTodo = values['todo'] + '\n'
                todos.append(newTodo.title())
                functions.writeTodos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            else:
                sg.popup('Please type a todo item to add!', font=('Helvetica', 20))
        case 'Edit':
            try:
                todoEdit = values['todos'][0]
                newTodo = values['todo']
                todos = functions.getTodos()
                index = todos.index(todoEdit)
                todos[index] = newTodo + '\n'
                functions.writeTodos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup('Please select a todo to edit!', font=('Helvetica', 20))
        case 'Complete':
            try:
                todoComplete = values['todos'][0]
                todos = functions.getTodos()
                todos.remove(todoComplete)
                functions.writeTodos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup('Please select a todo to complete!', font=('Helvetica', 20))
        case 'Exit':
            break
        case 'todos':
            itemSelected = values['todos'][0].strip('\n')
            window['todo'].update(value=itemSelected)
        case sg.WINDOW_CLOSED:
            break

print('Bye!!')
window.close()
