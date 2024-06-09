import glob

myFiles = glob.glob("files/*.txt")

print(myFiles)

for filePath in myFiles:
    with open(filePath, 'r') as file:
        print("------------------" + filePath + "---------------------")
        print(file.read())
