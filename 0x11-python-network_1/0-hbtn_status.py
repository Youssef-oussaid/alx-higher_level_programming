#!/usr/bin/python3
"""Fetches the status of a website"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status')\
            as response:
        content_bytes = response.read()
        content_str = content_bytes.decode('utf-8')
    print("Body response:")
    print("\t- type:", type(content_bytes))
    print("\t- content:", content_bytes)
    print("\t- utf8 content:", content_str)
