"""
Predefined input

"""


def list_to_str(l):
    return "\n".join(l)

class Auto:
    """
    Store all lines for testing.

    """


    def __init__(self):
        self.index = 0
        self.lines = []
        self.output = []
        self.expected = []


    def add(self, line):
        """
        Add line for test

        """
        self.lines.append(line)


    def expect(self, line):
        """
        Add line for expected outputs

        """
        self.expected.append(line)


    def line(self, prompt):
        """
        Override base method

        """

        result = self.lines[self.index]
        self.index = self.index+1
        return result


    def put(self, message):
        """
        Override base method

        """
        self.output.append(message)


    def result(self):
        if self.output == self.expected:
            result = [
                "Test passed:",
                list_to_str(self.output)
            ]
        else:
            result = [
                "Test failed",
                "Expected:",
                list_to_str(self.expected),
                "Got:",
                list_to_str(self.output)
            ]

        return list_to_str(result)
