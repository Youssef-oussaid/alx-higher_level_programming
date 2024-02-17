#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for k in sorted(a_dictionary.key()):
        print("{}: {}".format(k, a_dictionary))
