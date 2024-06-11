import functions
import FreeSimpleGUI as sg

label = sg.Text("Add a todo item: ")
inputBox = sg.InputText(tooltip="Enter todo")
addButton = sg.Button("Add")

window = sg.Window('My To-Do App', layout=[[label], [inputBox, addButton]])
window.read()
window.close()
