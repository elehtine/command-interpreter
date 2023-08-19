"""
Start read executed print loop (REPL)

"""

from commands import add, empty
from repl import loop


def main():
    """
    Start read executed print loop (REPL)

    """
    loop.start([add.execute, empty.execute])


if __name__ == "__main__":
    main()
