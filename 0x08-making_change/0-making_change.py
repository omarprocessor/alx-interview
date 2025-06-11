#!/usr/bin/python3
"""
Module to find the minimum number of coins needed
to make change for a given amount.
"""


def makeChange(coins, total):
    """
    Find the minimum number of coins needed to make change for a given amount.

    Args:
        coins (list): List of coin values
        total (int): Target amount to make change for

    Returns:
        int: Minimum number of coins needed, or -1 if not possible
    """
    # If total is 0 or less, return 0
    if total <= 0:
        return 0

    # Initialize dp array where dp[i] represents minimum coins needed
    # for amount i
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make 0 amount

    # Sort coins to optimize the solution
    coins.sort()

    # Fill the dp array
    for i in range(1, total + 1):
        for coin in coins:
            if coin > i:
                break
            if dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it means we couldn't make the change
    return dp[total] if dp[total] != float('inf') else -1
