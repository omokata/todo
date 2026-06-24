# todo.py

# `import` keyword import other python's module so that we can use 
# anything that is defined in that module. Basically module is just a python's
# file or collection of python's file.

import sys
import command_impl
import helper

COMMAND_VIEW = "view"
COMMAND_ADD = "add"
COMMAND_EDIT = "edit"
COMMAND_DELETE = "del"
COMMAND_HELP = "help"

# We can store function as value in dictionary
funcs = {
    COMMAND_VIEW: command_impl.todo_view,
    COMMAND_ADD: command_impl.todo_add,
    COMMAND_EDIT: command_impl.todo_edit,
    COMMAND_DELETE: command_impl.todo_delete,
    COMMAND_HELP: helper.help_message
}

command = COMMAND_HELP

args = sys.argv

if len(args) < 2:
    funcs[command]()
    exit(0)
else:
    args = args[1:]
    command = args[0]


if command == COMMAND_VIEW:
    funcs[command]()
elif command == COMMAND_ADD:
    if len(args) < 2:
        helper.help_message()
        exit(1)
    new_task = args[1]
    funcs[command](new_task)
elif command == COMMAND_EDIT:
    if len(args) < 3:
        helper.help_message()
        exit(1)
    task_id = args[1]
    try:
        task_id = int(task_id)
    except ValueError:
        print("argument task_id has to be an integer")
        exit(1)
    new_task = args[2]
    funcs[command](task_id, new_task)
elif command == COMMAND_DELETE:
    if len(args) < 2:
        helper.help_message()
        exit(1)
    task_id = args[1]
    try:
        task_id = int(task_id)
    except ValueError:
        print("argument task_id has to be an integer")
        exit(1)
    funcs[command](task_id)
elif command == COMMAND_HELP:
    helper.help_message()
else:
    print("Unknown command:", command)
    helper.help_message()
    exit(1)
