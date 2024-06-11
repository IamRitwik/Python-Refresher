import FreeSimpleGUI as sg

label1 = sg.Text("Select files to compress: ")
input1 = sg.Input()
chooseButton1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
chooseButton2 = sg.FolderBrowse("Choose")

compressButton = sg.Button("Compress")

window = sg.Window("File Compressor", layout=[[label1, input1, chooseButton1],
                                              [label2, input2, chooseButton2],
                                              [compressButton]])

window.read()
window.close()
