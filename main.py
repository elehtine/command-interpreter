"""
Start read executed print loop (REPL)

"""


from commands import add, empty, invalid
from repl import loop
from user_interface.cli import Input


def main():
    """
    Start read executed print loop (REPL)

    """

    user_interface = Input()
    loop.start(user_interface, [add.execute, empty.execute, invalid.execute])


if __name__ == "__main__":
    main()
