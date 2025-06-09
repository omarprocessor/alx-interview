# 0x07. Rotate 2D Matrix

## Description
This project implements an in-place algorithm to rotate an `n x n` 2D matrix by 90 degrees clockwise using Python. The operation is done without using any additional memory for another matrix.

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- Python 3.8.10 on Ubuntu 20.04 LTS
- First line of all files: `#!/usr/bin/python3`
- `pycodestyle` (version 2.8.0) compliance
- No imports allowed
- No return values; the matrix is modified in-place
- All files must be executable
- All functions must be documented

## Concepts
- **Matrix Transposition**: Swap rows with columns.
- **Reverse Rows**: After transposing, reverse each row to complete the 90° rotation.
- **In-place Operation**: Modify the matrix directly to save space.

## File Structure

0x07-rotate_2d_matrix/
├── 0-rotate_2d_matrix.py
├── main_0.py
└── README.md