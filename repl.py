"""
Define REPL loop

Loop is used in all commands.

"""


def loop(commands):
    """
    Loop for REPL

    Returns
    -------
    status
    """

    print("--- Loop start ---")
    while True:
        line = input("> ")

        if not line:
            break

        status = None
        for command in commands:
            status = command(line)
        if status:
            break

    print("--- Loop end ---")
    return status
