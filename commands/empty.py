"""
Empty command

Can be used two quit.

"""

from repl.status import Status

def execute(line):
    """
    Identifies empty line

    Parameters
    ----------
    line : command

    Returns
    -------
    status : True for empty line

    """

    status = Status()
    if line == "":
        print("Empty line: exit")
        status.end("exit")
    return status
