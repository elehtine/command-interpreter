"""
Define REPL

"""


def loop():
    """
    Loop for REPL

    """

    print("Program start!")
    while True:
        line = input("> ")
        if not line:
            break

        print(line)
    print("Program end!")
