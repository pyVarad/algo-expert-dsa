#!/usr/bin/env python
"""
Monotonic Array
Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.
An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entirely non-decreasing.
Non-increasing elements aren't necessarily exclusively decreasing; they simply don't increase. Similarly, non-decreasing elements aren't necessarily exclusively increasing; they simply don't decrease.
Note that empty arrays and arrays of one element are monotonic.

Sample Input
array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

Sample Output
View site information

true
"""

# Time complexity O(n) and space complexity is O(n)
def isMonotonic(array):
    start_ptr = 0
    adj_ptr = 1
    direction = {}
    
    while adj_ptr < len(array):
        if array[start_ptr] > array[adj_ptr]:
            direction["dec"] = True
        elif array[start_ptr] == array[adj_ptr]:
            direction["equals"] = True
        else: 
            direction["inc"] = True

        start_ptr += 1
        adj_ptr += 1
    
    if "equals" in direction:
        del direction["equals"]
    return len(direction) <= 1

if __name__ == "__main__":
    res = isMonotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001])
    print(res)