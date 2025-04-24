#!/usr/bin/env python
"""
Write a function that takes in an array of at least two integers and that returns an array of the starting and ending indices of the smallest subarray in the input array that needs to be sorted in place in order for the entire input array to be sorted (in ascending order).

If the input array is already sorted, the function should return [-1, -1] -

Sample Input
array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
Sample Output
[3, 9]
"""

from typing import List

def subarray_sort(array: List[int]) -> List[int]:
    min_out_of_order = float("inf")
    max_out_of_order = float("-inf")

    # Find the positions where the array elements go off the order.
    # Record the elements and not the index. This is because we need to 
    # identify the position of the recorded element in the sorted list.

    for pos in range(len(array)):
        if is_out_of_order(pos, array):
            min_out_of_order = min(min_out_of_order, array[pos])
            max_out_of_order = max(max_out_of_order, array[pos])

    # If the min out of order has not changed with initalized value 
    # then it means the array is already sorted.
    if min_out_of_order == float("inf"):
        return [1, -1]
    
    ptr_for_locating_min_index = 0    
    ptr_for_locating_max_index = len(array) - 1

    # Traverse the array to find the correct position of minumum number.
    while array[ptr_for_locating_min_index] < min_out_of_order:
          ptr_for_locating_min_index += 1

    # Traverse the array to find the correct position of maximum number.
    while array[ptr_for_locating_max_index] > max_out_of_order:
        ptr_for_locating_max_index -= 1

    return [ptr_for_locating_min_index, ptr_for_locating_max_index]


def is_out_of_order(pos: int, a: List[int]):
    if pos == 0:
        return a[pos] > a[pos + 1]
    elif pos == len(a) - 1:
        return a[pos] < a[pos - 1]
    else:
        return (a[pos] > a[pos + 1]) or (a[pos] < a[pos - 1])
    
if __name__ == "__main__":
    result = subarray_sort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19])