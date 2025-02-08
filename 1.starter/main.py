todos = []
while True:
    action = input("Type add/show/edit/complete or exit: ")
    match action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            # file = open('files/todos.txt', 'r')
            # todos = file.readlines()
            # file.close()

            # using context manager
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo.capitalize())

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
        case 'show':
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            # newTodos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{index + 1}-{item}")
        case 'edit':
            number = input("Enter number of todo item you want to edit: ")
            number = int(number)
            number = number - 1
            newTodo = input("Enter new todo: ")
            newTodo = newTodo.capitalize()
            todos[number] = newTodo + '\n'

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
        case 'complete':
            number = input("Enter number of todo you want to complete: ")
            number = int(number)

            completedTodo = todos[number - 1].strip('\n')
            todos.pop(number - 1)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

            print(f"Todo {completedTodo} was completed!")
        case 'exit':
            break
        case whatever:
            print("Hey! You entered a wrong command!")

print('Bye!!')
