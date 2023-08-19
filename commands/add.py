"""
Add two numbers together

"""

from repl import loop

def execute(line):
    """
    Start loop for asking two numbers and print sum

    """

    if line != "add":
        return

    print("Give two integer")
    first = loop.start([loop.read_int], mark="first: ")
    second = loop.start([loop.read_int], mark="second: ")

    print(f"{first} + {second} = {first + second}")
