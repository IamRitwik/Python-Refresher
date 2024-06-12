import FreeSimpleGUI as sg
from zipCreator import makeArchive

label1 = sg.Text("Select files to compress: ")
input1 = sg.Input()
chooseButton1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
chooseButton2 = sg.FolderBrowse("Choose",key="folder")

compressButton = sg.Button("Compress")
outputLabel = sg.Text(key="output", text_color="green")

window = sg.Window("File Compressor", layout=[[label1, input1, chooseButton1],
                                              [label2, input2, chooseButton2],
                                              [compressButton, outputLabel]], font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event, values)
    filePaths = values['files'].split(";")
    print(filePaths)
    folder = values['folder']
    print(folder)
    makeArchive(filePaths, folder)
    window["output"].update(value="Archive completed!")

window.close()
