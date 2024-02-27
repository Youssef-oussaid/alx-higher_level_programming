#!/usr/bin/python3
"""Define a locked class"""


class LockedClass:
    """Prevents the user from instancing new LockedClass attribute
    for anything but the one called 'first_name'
    """
    __slots__ = ["first_name"]
