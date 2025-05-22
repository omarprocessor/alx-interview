#!/usr/bin/python3
"""
Solves the N Queens problem.
"""
import sys


def is_safe(queens, row, col):
    """Check if it's safe to place a queen at (row, col)."""
    for r, c in queens:
        if c == col or r - c == row - col or r + c == row + col:
            return False
    return True


def solve_nqueens(n, row=0, queens=[], solutions=[]):
    """Recursively solves the N Queens puzzle."""
    if row == n:
        solutions.append(queens[:])
        return

    for col in range(n):
        if is_safe(queens, row, col):
            queens.append([row, col])
            solve_nqueens(n, row + 1, queens, solutions)
            queens.pop()


def main():
    """Entry point of the program."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    solve_nqueens(n, 0, [], solutions)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
