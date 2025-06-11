# Making Change Problem

This directory contains the solution to the coin change problem where we need to find the minimum number of coins required to make change for a given amount.

## Problem Description

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

## Files

- [0-making_change.py](0-making_change.py): Contains the implementation of the makeChange function
- [0-main.py](0-main.py): Test file demonstrating the usage of makeChange function

## Requirements

- Python 3.4.3
- Ubuntu 20.04 LTS
- PEP 8 style guide (version 1.7.x)

## Usage

1. Ensure you have Python 3.4.3 installed
2. Make the Python files executable:
   ```bash
   chmod +x *.py
   ```
3. Run the test file:
   ```bash
   python3 0-main.py
   ```

## Function Prototype

```python
def makeChange(coins, total)
```

### Parameters
- `coins`: List of coin values (integers)
- `total`: Target amount to make change for (integer)

### Returns
- Minimum number of coins needed to make the total amount
- 0 if total is 0 or less
- -1 if the total cannot be made with the given coins

## Example

```python
print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
```

## Constraints

- Coin values will always be integers greater than 0
- Assume infinite supply of each coin denomination
- Total can be any non-negative integer

## Solution Approach

The solution uses dynamic programming to efficiently find the minimum number of coins needed. It builds up solutions for smaller amounts to solve the total amount, ensuring optimal runtime performance.
