def getAverage():
    with open("files/data.txt") as file:
        data = file.readlines()
    values = data[1:]
    values = [float(v) for v in values]
    averageTemp = sum(values) / len(values)
    return averageTemp


average = getAverage()
print(average)
