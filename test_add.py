"""
Test file for add command

"""


from repl import loop
from commands import add, empty
from user_interface.auto import Auto


def main():
    """
    Test function

    """

    auto = Auto()
    auto.add("add")
    auto.expect("Give two integers")
    auto.add("one")
    auto.expect("Invalid number: one")
    auto.add("1")
    auto.add("2")
    auto.expect("1 + 2 = 3")
    auto.add("")
    auto.expect("Empty line: exit")
    loop.start(auto, [add.execute, empty.execute])
    print(auto.result())


if __name__ == "__main__":
    main()
