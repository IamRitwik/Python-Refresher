import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    action = input("Type add/show/edit/complete or exit: ").strip()

    if action.startswith('add'):
        todo = action[4:] + '\n'
        todos = functions.getTodos()
        todos.append(todo.title())
        functions.writeTodos(todos)

    elif action.startswith('show'):
        todos = functions.getTodos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}-{item}")

    elif action.startswith('edit'):
        try:
            number = int(action[5:])
            number = number - 1
            todos = functions.getTodos()
            newTodo = input("Enter new todo: ")
            newTodo = newTodo.title()
            todos[number] = newTodo + '\n'
            functions.writeTodos(todos)
        except ValueError:
            print("You have entered invalid command")
            continue
        except IndexError:
            print("There is no todo item with that number!")
            continue

    elif action.startswith('complete'):
        try:
            number = int(action[9:])
            todos = functions.getTodos()
            completedTodo = todos[number - 1].strip('\n')
            todos.pop(number - 1)
            functions.writeTodos(todos)
            print(f"Todo {completedTodo} was completed!")
        except IndexError:
            print("There is no todo item with that number!")
            continue
        except ValueError:
            print("You have entered invalid command")
            continue

    elif action.startswith('exit'):
        break
    else:
        print("Hey! You entered a wrong command!")

print('Bye!!')
