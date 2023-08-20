"""
Add two numbers together

"""

from repl import loop
from repl.status import Status

def execute(line):
    """
    Start loop for asking two numbers and print sum

    """

    if line != "add":
        return Status()

    print("Give two integer")
    first = loop.start([loop.read_int], mark="first: ")
    second = loop.start([loop.read_int], mark="second: ")
    result = first.value + second.value

    print(f"{first} + {second} = {result}")
    return Status(True, result)
