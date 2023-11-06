FILEPATH = r"C:\Users\acald\Documents\Python\TODO\todos.txt"

def get_todos(filepath=FILEPATH):
    """ read a text file and return the
     list of to-do items. """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """write the to-do items list in the next file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)