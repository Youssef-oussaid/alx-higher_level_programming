#!/usr/bin/python3
def islower(c):
    if ord(c) > 96 and ord(c) < 123:
        return True
    else:
        return False

def uppercase(str):
    for c in str:
        print("{:c}"
              .format(ord(c) if not islower(c) else ord(c) - 32),
              end="")
    print("")
