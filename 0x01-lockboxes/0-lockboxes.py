#!/usr/bin/python3
"""Module to determine if all boxes can be unlocked."""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
        boxes (list of lists): Each box contains a list of keys.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    unlocked = [False] * len(boxes)
    unlocked[0] = True
    stack = [0]

    while stack:
        current = stack.pop()
        for key in boxes[current]:
            if key < len(boxes) and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)

    return all(unlocked)
