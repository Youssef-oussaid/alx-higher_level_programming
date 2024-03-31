#!/usr/bin/python3
"""Module"""


class MyList(list):
    """CLass MyList with the inheritance"""

    def print_sorted(self):
        """prints a list in a sorted manner"""

        print(sorted(list(self)))
