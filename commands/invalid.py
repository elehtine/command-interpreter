"""
Invalid command message

"""

from repl import status

def execute(line):
    """
    Print invalid command message
    """

    print(f"Invalid command: {line}")
    return status.Status()
