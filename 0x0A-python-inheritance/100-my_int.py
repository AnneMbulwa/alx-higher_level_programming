#!/usr/bin/python3
"""class myint that inherits from int"""



class MyInt(int):
    """class myint
    Args
        is a rebel
        has == and !=
        """
    def __eq__(self, x):
        return self.real != x

    def __ne__(self, x):
        return self.real == x
