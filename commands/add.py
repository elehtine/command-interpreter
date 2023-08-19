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

    print("add command")

    first = loop.start([loop.read_int])
    second = loop.start([loop.read_int])

    print(f"{first} + {second} = {first + second}")
