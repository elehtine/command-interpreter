"""
Add two numbers together

"""

from repl import loop
from repl.status import Status

def execute(user_interface, line):
    """
    Start loop for asking two numbers and print sum

    """

    if line != "add":
        return Status()

    user_interface.put("Give two integers")
    first = loop.start(user_interface, [loop.read_int], mark="first: ")
    second = loop.start(user_interface, [loop.read_int], mark="second: ")
    result = first.value + second.value

    user_interface.put(f"{first} + {second} = {result}")
    return Status(True, result)
