#!/usr/bin/python3
"""Fetches the status of a website"""
import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    email = argv[2]
    data = urllib.parse.urlencode({'email': argv[2]}).encode('utf-8')
    req = urllib.request.Request(argv[1], data=data, method='POST')
    with urllib.request.urlopen(argv[1]) as f:
        print(f"Your email is: {email}")
