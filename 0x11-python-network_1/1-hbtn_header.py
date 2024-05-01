#!/usr/bin/python3
"""Fetches the status of a website"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        for header, value in response.headers.items():
            if header == "X-Request-Id":
                print(value)
