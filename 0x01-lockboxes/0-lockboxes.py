#!/usr/bin/python3

def canUnlockAll(boxes):
    # Initialize a list to track which boxes have been unlocked
    unlocked = [False] * len(boxes)
    unlocked[0] = True  # The first box is always unlocked
    
    # List to track boxes that we still need to check
    stack = [0]
    
    # Iterate through the boxes we can open (using the stack to simulate DFS)
    while stack:
        current_box = stack.pop()
        
        # For each key in the current box, if it hasn't been unlocked, unlock it
        for key in boxes[current_box]:
            if key < len(boxes) and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)
    
    # Check if all boxes have been unlocked
    return all(unlocked)
