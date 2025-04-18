#!/usr/bin/env python
"""
Move Element To End
You're given an array of integers and an integer. Write a function that moves all instances of that integer
in the array to the end of the array and returns the array.The function should perform this in place
(i.e., it should mutate the input array) and doesn't need to maintain the order of the other integers.

Sample Input
array
= [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2
Sample Output
[1, 3, 4, 2, 2, 2, 2, 2] // the numbers 1, 3, and 4 could be ordered differently
"""

from typing import List

# Time complexity O(n) and Space complexity O(1)
def move_elements_to_end(array: List[int], element: int):
    left_ptr = 0
    right_ptr = len(array) - 1

    while left_ptr <= right_ptr:
        # Remember this edge condition.
        while left_ptr < right_ptr and array[right_ptr] == element:
            right_ptr -= 1

        if array[left_ptr] == element:
            array[left_ptr], array[right_ptr] = array[right_ptr], array[left_ptr]

        left_ptr += 1

    return array

# Time Complexity O(n) and Space Complexity O(1)
def move_elements_to_end_alternative(array: List[int], element: int):
    ptr = 0
    for pos, arr_element in enumerate(array):
        if arr_element != element:
            array[pos], array[ptr] = array[ptr], array[pos]
            ptr += 1
    
    return array


if __name__ == "__main__":
    # res = move_elements_to_end([2, 1, 2, 2, 2, 3, 4, 2], 2)
    # print(res)
    res = move_elements_to_end_alternative([2, 1, 2, 2, 2, 3, 4, 2], 2)
    print(res)
