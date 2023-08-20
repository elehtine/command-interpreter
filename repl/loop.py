"""
Define REPL functions

Loop is used in all commands.

"""

from repl.status import Status

def start(commands, mark="> "):
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
        line = input(mark)

        for command in commands:
            status = command(line)
            if status.value is not None:
                break

    return status


def read_int(line):
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
        print(f"Invalid number: {line}")
    return status
