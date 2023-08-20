"""
Test file for invalid command

"""


from repl import loop
from commands import invalid, empty
from user_interface.auto import Auto


def main():
    """
    Test function

    """

    auto = Auto()
    command = "foo"
    auto.add(command)
    auto.expect(f"Invalid command: {command}")
    auto.add("")
    auto.expect("Empty line: exit")
    loop.start(auto, [empty.execute, invalid.execute])
    print(auto.result())


if __name__ == "__main__":
    main()
