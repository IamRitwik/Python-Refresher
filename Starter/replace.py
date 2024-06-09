fileNames = ["1.RawData.txt", "2.Reports.txt", "3.Presentation.txt"]

# Lists are mutable
# Strings are immutable
# Tuples are immutable version of list

for fileName in fileNames:
    newFileName = fileName.replace('.', '-', 1)
    print(newFileName, fileName)
    index = fileNames.index(fileName)
    fileNames[index] = newFileName

print(fileNames)
print('-----------------------------------------------------------------------------------------')

fileNameList = ["1.RawData.txt", "2.Reports.txt", "3.Presentation.txt"]
print(fileNameList)

fileNameList = [fileName.replace('.', '-', 1) for fileName in fileNameList]
print(fileNameList)

print('-----------------------------------------------------------------------------------------')


files = ["1.Java", "2.Python", "3.JavaScript"]
print(files)

files = [fileName.replace('.', '-') + '.txt' for fileName in files]
print(files)