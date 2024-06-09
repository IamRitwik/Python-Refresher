waitingList = ['sean', 'ben', 'john']
waitingList.sort()

for index, item in enumerate(waitingList):
    print(f"{index+1}.{item.capitalize()}")

filenames = ['document', 'report', 'presentation']
for index, item in enumerate(filenames):
    print(f"{index}-{item.capitalize()}.txt")
