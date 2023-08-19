"""
Start read executed print loop (REPL)

"""

from commands import add
from repl import loop


def main():
    """
    Start read executed print loop (REPL)

    """
    loop.start([add.execute])


if __name__ == "__main__":
    main()
