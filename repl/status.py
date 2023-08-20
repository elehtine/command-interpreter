"""
Status for read execute print loop

"""


class Status:
    """
    run : Continue running next loop
    value : Return value of loop

    """


    def __init__(self, run=True, value=None):
        self.run = run
        self.value = value


    def end(self, value):
        """
        Set run to false

        """
        self.run = False
        self.value = value


    def __str__(self):
        return str(self.value)
