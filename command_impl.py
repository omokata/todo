# command.py
# This file will be the place where we define our functionality to
# view, add, edit and delete todo task. Yes we can separate the file
# and import this file into todo.py. Cool!

import helper

todo = []
STORAGE_PATH = "/home/muhdamin/.my_todo.txt"

# this is a wrapper.
# because each function need to perform the same
# thing before doing what their own task,
# we can wrap the function so that it call another function
# before calling the function we want to call
# we can use this either directly passing the function we want in it, or
# using the `@`. It's called a decorator
def _init(func):
    def wrapper(*args, **kwargs):
        helper.init_todo(todo, STORAGE_PATH)
        func(*args, **kwargs)
    return wrapper


@_init
def todo_view():
    for i, task in enumerate(todo):
        print(f"{i + 1}. {task}", end="")


@_init
def todo_add(new_task):
    print(f"Added \"{new_task}\" to todo")
    todo.append(new_task)
    helper.save_todo(todo, STORAGE_PATH)


@_init
def todo_edit(task_id, new_task):
    assert type(task_id) == int
    if (task_id > len(todo)):
        print("No task to edit")
        return
    if (task_id < 1):
        print("range should be from 1 onwards")
        return
    print("Edited successfully")
    todo[task_id - 1] = new_task
    helper.save_todo(todo, STORAGE_PATH)


@_init
def todo_delete(task_id):
    assert type(task_id) == int
    if (task_id > len(todo)):
        print("No task to delete")
        return
    if (task_id < 1):
        print("range should be from 1 onwards")
        return
    task = todo[task_id - 1]
    del todo[task_id - 1]
    print(f"Deleted {task_id}. {task}")
    helper.save_todo(todo, STORAGE_PATH)
