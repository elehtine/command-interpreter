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

    first = loop([read_int])
    second = loop([read_int])

    print(f"{first} + {second} = {first + second}")


def read_int(line):
    """
    Returns
    -------
    int, None : parsed integer

    """

    value = None
    try:
        value = int(line)
    except ValueError:
        print(f"Invalid number: {line}")
    return value
