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

    # Sort coins in descending order for optimization
    coins.sort(reverse=True)

    # Initialize dp array where dp[i] represents minimum coins needed
    # for amount i
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make 0 amount

    # Process each coin
    for coin in coins:
        # Update dp array starting from the coin value
        for i in range(coin, total + 1):
            # Skip if current amount can't be made with this coin
            if dp[i - coin] == float('inf'):
                continue
            # Update dp[i] only if we can make a better solution
            if dp[i] == float('inf') or dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1

    # If dp[total] is still infinity, it means we couldn't make the change
    return dp[total] if dp[total] != float('inf') else -1
