#!/usr/bin/python3
"""
12. My integer
"""


class MyInt(int):
    """
    MyInt class
    """
    def __eq__(self, other):
        """
        eq method
        """
        return False

    def __ne__(self, other):
        """
        ne method
        """
        return True
