todos = []


def showTodos():
    for item in todos:
        print(item)


while True:
    action = input("Type add or show or exit: ").strip()
    match action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo.capitalize())
        case 'show':
            showTodos()
        case 'exit':
            break
        case whatever:
            print("Hey! You entered a wrong command!")

print('Bye!!')
