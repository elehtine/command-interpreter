"""
Define REPL functions

Loop is used in all commands.

"""


def start(commands, mark="> "):
    """
    Start loop for REPL

    Execute commands in the loop. Every command is executed once per cycle.
    Loop is running while status is None.

    Parameters
    ----------
    commands : list of commands

    Returns
    -------
    status
    """

    print("--- Loop start ---")
    status = None
    while status is None:
        line = input(mark)

        for command in commands:
            status = command(line)

    print("--- Loop end ---")
    return status


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
