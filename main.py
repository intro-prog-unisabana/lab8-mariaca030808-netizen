"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO: Implementar CLI según README.md
import sys
from todo_manager import read_todo_file, write_todo_file

Hay_error= False

if len(sys.argv) < 2:
    print("Insufficient arguments provided!")
    Hay_error = True

if not Hay_error:
    if sys.argv[1]== "--help":
        print("""Usage: python main.py <file_path> <command> [arguments]...

Commands:
  add "task"    - Add a task to the list.
  remove "task" - Remove a task from the list.
  view          - Display all tasks.

Examples:
  python main.py tasks.txt add "Buy groceries"
  python main.py tasks.txt remove "Do laundry"
  python main.py tasks.txt view
  python main.py tasks.txt add "Call mom" remove "Take out trash" view""")

    else:
        file_path= sys.argv[1]
        Tareas= read_todo_file(file_path)

        items= 2
        while items < len(sys.argv) and not Hay_error:
            commandousuario = sys.argv[items]

            if commandousuario== "view":
                print("Tasks:")
                for task in Tareas:
                    print(task)
                items = items + 1

            elif commandousuario== "add":
                if items + 1 >= len(sys.argv):
                    print('Task description required for "add".')
                    Hay_error = True
                else:
                    new_task= sys.argv[items + 1]
                    Tareas.append(new_task)
                    print(f'Task "{new_task}" added.')
                    items= items + 2

            elif commandousuario== "remove":
                if items + 1 >= len(sys.argv):
                    print('Task description required for "remove".')
                    Hay_error= True
                else:
                    task_to_remove = sys.argv[items + 1]
                    try:
                        Tareas.remove(task_to_remove)
                        print(f'Task "{task_to_remove}" removed.')
                    except ValueError:
                        print(f'Task "{task_to_remove}" not found.')
                    items= items + 2

            else:
                print("Command not found!")
                Hay_error= True

        if not Hay_error:
            write_todo_file(file_path, Tareas)