FILEPATH = 'todos.txt'


def getTodos(filePath=FILEPATH):
    """
    Read a text file and return the List of
    todo items
    """
    with open(filePath, 'r') as getTodoFile:
        todoList = getTodoFile.readlines()
    return todoList


def writeTodos(todoSArg, filePath=FILEPATH):
    """ Write todo items List in text file """
    with open(filePath, 'w') as writeTodoFile:
        writeTodoFile.writelines(todoSArg)


print(__name__)
if __name__ == "__main__":
    print(getTodos())
