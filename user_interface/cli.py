"""
Command line interface

"""


class Input:
    """
    Read and put lines

    """


    def __init__(self):
        pass


    def line(self, prompt):
        return input(prompt)


    def put(self, message):
        print(message)
