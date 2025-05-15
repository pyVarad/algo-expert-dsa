"""
Non-Constructible Change
Given an array of positive integers representing the values of coins in your possession, write a function that returns the minimum amount of change (the minimum sum of money) that you cannot create. The given coins can have any positive integer value and aren't necessarily unique (i.e., you can have multiple coins of the same value).
For example, if you're given coins = [1, 2, 5], the minimum amount of change that you can't create is 4. If you're given no coins, the
minimum amount of change that you can't create is
1
Sample Input
coins = [5, 7, 1, 1, 2, 3, 22]
Sample Output
20
"""
from typings import List

# Space complexity is O(1) and time complexity is O(nlogn)
def non_constructible_change(coins: List):
    coins.sort()
    change = 1
    for x in coins:
        if x - change <= 0:
            change += x
        else:
            break
    
    return change


if __name__ == "__main__":
  non_constructible_change([5, 7, 1, 1, 2, 3, 22])
