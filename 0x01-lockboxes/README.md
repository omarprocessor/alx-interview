0x01. Lockboxes - README
Project Overview
In this project, you are tasked with determining if all the locked boxes can be opened. Given n number of locked boxes, each numbered sequentially from 0 to n - 1, and a set of keys, your goal is to write a method that determines whether all the boxes can be opened.

Each box may contain keys that open other boxes. The first box (boxes[0]) is unlocked initially. The challenge is to check whether all the boxes can be opened using the available keys.

Task Requirements
You will need to implement the function canUnlockAll(boxes) that determines if all boxes can be opened. Here's what you need to know:

Prototype
python
Copy
Edit
def canUnlockAll(boxes):
Arguments
boxes is a list of lists, where each list contains integers representing keys to open other boxes. For example, boxes[0] contains the keys that can open other boxes.

Key Points
A key with the same number as a box opens that box.

The first box boxes[0] is unlocked initially.

Return True if all the boxes can be opened, otherwise return False.

Constraints
All keys will be positive integers.

There can be keys that do not have corresponding boxes.

It is guaranteed that the first box boxes[0] is unlocked.

Algorithm
This problem can be thought of as a graph traversal problem. You will need to traverse the boxes using the keys provided. A graph traversal algorithm like Depth-First Search (DFS) or Breadth-First Search (BFS) could be used to explore all the boxes that can be opened with the available keys.

Steps:
Start by unlocking the first box (boxes[0]).

Collect all the keys from this box.

Use the collected keys to unlock other boxes.

Repeat the process until no more boxes can be unlocked or all boxes are unlocked.

If all boxes are unlocked, return True; otherwise, return False.

Requirements
Python 3: This project is intended to be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3).

PEP 8: All your code should adhere to PEP 8 style guide.

Executable files: Ensure all your files are executable.

No indentation: Your code should follow the guidelines of no indentation for certain styles.

Example
Here’s a sample test case for the canUnlockAll() function:

python
Copy
Edit
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))
# Expected output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))
# Expected output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
# Expected output: False
Output:
bash
Copy
Edit
True
True
False
Resources
Concepts to Review:
Lists and List Manipulation: Understanding how to manipulate lists in Python, including accessing elements, iterating, and modifying lists.

Graph Theory: Knowledge of graph traversal algorithms (like BFS/DFS) could help in solving the problem efficiently.

Algorithmic Complexity: Be aware of the time and space complexity of your solution.

Recursion and Stack: Recursive approaches may be necessary for traversing the boxes and keys.

Set Operations: Sets can help keep track of visited boxes and available keys.

Helpful Resources:
Python Lists (Python Official Documentation)

Graph Theory (Khan Academy)

Big O Notation (GeeksforGeeks)

Recursion in Python (Real Python)

Python Queue and Stack (GeeksforGeeks)

Python Sets (Python Official Documentation)

Project Files
File Structure:
0-lockboxes.py: Contains the solution to the problem.

main_0.py: File used to test the solution with example inputs.

Instructions:
Clone the repository or navigate to the 0x01-lockboxes directory.

Implement the function canUnlockAll(boxes) inside 0-lockboxes.py.

Make sure the file is executable.

Test your code using the provided examples or your own test cases.

Conclusion
By the end of this project, you should have a strong understanding of graph traversal techniques, as well as how to apply Python's data structures such as lists, sets, and recursion to solve algorithmic challenges efficiently.
