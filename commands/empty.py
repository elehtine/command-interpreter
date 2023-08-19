"""
Empty command

Can be used two quit.

"""


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
    
    return True if line == "" else None

