# 0x05. N Queens

## Background

The **N Queens puzzle** is a classic backtracking problem that challenges you to place `N` non-attacking queens on an `N×N` chessboard. A queen can attack another queen if it is on the same row, column, or diagonal.

This project solves the N Queens problem using backtracking in Python.

---

## Requirements

- Only the `sys` module is allowed.
- The program must handle input validation.
- The output should print all possible solutions.
- One solution per line, with coordinates of queens.

---

## Usage

```bash
./0-nqueens.py N
```

### Arguments

- If the user does not provide exactly one argument, print:
  ```
  Usage: nqueens N
  ```
  and exit with status `1`.

- If `N` is not an integer, print:
  ```
  N must be a number
  ```
  and exit with status `1`.

- If `N` is less than `4`, print:
  ```
  N must be at least 4
  ```
  and exit with status `1`.

---

## Output Format

Each solution should be printed on a new line as a list of coordinate pairs:

```bash
[[row, column], [row, column], ..., [row, column]]
```

### Example

```bash
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]

$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

---

## Files

- `0-nqueens.py`: Main program that solves the N Queens problem.

---

## Author

Project done as part of the ALX SE program.

---

## References

- [Backtracking](https://en.wikipedia.org/wiki/Backtracking)
- [N-Queens Problem](https://en.wikipedia.org/wiki/Eight_queens_puzzle)
