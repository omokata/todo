# helper.py

def help_message():
    print("Usage: todo <command> [args]")
    print("command [args]:")
    print("  - help")
    print("  - view")
    print("  - add 'new task'")
    print("  - edit task_id 'new_edited_task'")
    print("  - del task_id")


def init_todo(todo, storage_path):
    """
    load task from storage_path.
    The storage format is as follow:
    1. task1
    2. my task
    3. your task
    """
    assert type(todo) == list
    assert type(storage_path) == str
    try:
        with open(storage_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                # format `1. my task is this` to
                # `my task is this` and append to
                # todo
                if line.isspace():
                    continue
                todo.append(" ".join(line.split(" ")[1:]))
    except FileNotFoundError as err:
        print(f"{storage_path} not found! creating file...")
        with open(storage_path, "w"):
            pass
    except OSError as err:
        print(f"Failed to load todo task from storage: {str(err)}")
        exit(1)


def save_todo(todo, output_path):
    """
    Save todo in output_path in format:
    1. my task is this
    2. I hate doing my task
    3. foo bar baz
    """
    assert type(todo) == list
    assert type(output_path) == str
    
    try:
        with open(output_path, "w") as f:
            for i, task in enumerate(todo):
                f.write(f"{i+1}. {task.rstrip()}\n")
    except Exception as err:
        print(f"Failed to save todo to storage path: {str(err)}")
        exit(1)
