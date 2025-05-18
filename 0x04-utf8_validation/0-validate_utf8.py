#!/usr/bin/python3
"""
This module contains a
method that determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Check if a list of integers represents a valid UTF-8 encoding.
    """
    n_bytes = 0

    for byte in data:
        byte = byte & 0xFF

        if n_bytes == 0:
            if byte >> 5 == 0b110:
                n_bytes = 1
            elif byte >> 4 == 0b1110:
                n_bytes = 2
            elif byte >> 3 == 0b11110:
                n_bytes = 3
            elif byte >> 7:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            n_bytes -= 1

    return n_bytes == 0
