"""
Define REPL functions

Loop is used in all commands.

"""

from repl.status import Status

def start(user_interface, commands, mark="> "):
    """
    Start loop for REPL

    Execute commands in the loop. Loop is running while status is runnning.

    Parameters
    ----------
    commands : list of commands
    mark : input marker

    Returns
    -------
    status
    """

    status = Status()

    while status.run:
        line = user_interface.line(mark)

        for command in commands:
            status = command(user_interface, line)
            if status.value is not None:
                break

    return status


def read_int(user_interface, line):
    """
    Returns
    -------
    int, None : parsed integer

    """

    status = Status()
    try:
        value = int(line)
        status.end(value)
    except ValueError:
        user_interface.put(f"Invalid number: {line}")
    return status
