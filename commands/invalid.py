"""
Invalid command message

"""

from repl import status

def execute(user_interface, line):
    """
    Print invalid command message
    """

    user_interface.put(f"Invalid command: {line}")
    return status.Status()
