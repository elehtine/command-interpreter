"""
Test file for empty command

"""


from repl import loop
from commands import empty
from user_interface.auto import Auto


def main():
    """
    Test function

    """

    auto = Auto()
    auto.add("")
    auto.expect("Empty line: exit")
    loop.start(auto, [empty.execute])
    print(auto.result())


if __name__ == "__main__":
    main()
