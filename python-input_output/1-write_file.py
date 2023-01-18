#!/usr/bin/python3
"""write file"""


def write_file(filename="", text=""):
    """writing a text"""
    if filename:
        with open(filename, mode='w', encoding="utf-8") as f:
            for i in f:
                print(i.write(text))
