"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO: Implementar CLI según README.md

from asyncio import tasks
import sys
from todo_manager import read_todo_file, write_todo_file

try:
    if len(sys.argv) < 2:
        raise IndexError("Insufficient arguments provided!")
    else:
        file_path = sys.argv[1]
        Tareas= read_todo_file(file_path)
        items= 2
        while items < len(sys.argv):
            command = sys.argv[items]
            if command == "view":
                print("Tasks:")
                for task in Tareas:
                    print(task)
                items= items + 1

            elif command== "add":
                if items + 1 >= len(sys.argv):
                    raise IndexError('Task description required for "add".')

                new_task= sys.argv[items + 1]
                Tareas.append(new_task)
                print(f'Task "{new_task}" added.')
                items= items + 2  

            elif command== "remove":
                if items + 1 >= len(sys.argv):
                    raise IndexError('Task description required for "remove".')

                task_to_remove= sys.argv[items + 1]
                try:
                    Tareas.remove(task_to_remove)
                    print(f'Task "{task_to_remove}" removed.')
                except ValueError:
                    print(f'Task "{task_to_remove}" not found.')

                items= items + 2
            else:
                 ValueError("Command not found!")

        write_todo_file(file_path, Tareas)
except IndexError as error:
    print(f"Error: {error}")