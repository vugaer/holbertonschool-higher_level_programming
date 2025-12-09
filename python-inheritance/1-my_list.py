#!/usr/bin/python3
"""to run doctest

python3 -m doctest -v tests/1-my_list.txt"""


class MyList(list):
    """MyList class that inherits from list"""
    
    def print_sorted(self):
        """Prints the list in sorted ascending order"""
        print(sorted(self))
