#!/usr/bin/python3
from hidden_4 import *

if __name__ == "__main__":
    names = [name for name in dir() if not name.startswith("__")]
    names.sort()
    for name in names:
        print(name)
