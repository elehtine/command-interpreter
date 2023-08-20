"""
Empty command

Can be used two quit.

"""

from repl.status import Status

def execute(user_interface, line):
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
        user_interface.put("Empty line: exit")
        status.end("exit")
    return status
