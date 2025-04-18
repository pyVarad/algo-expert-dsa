#!/usr/bin/env python
"""
Sorted Squared Array

Write a function that takes in a non-empty array of integers that are sorted in ascending order and
returns a new array of the same length with the squares of the original integers also sorted in ascending order.

Sample Input
array = [1, 2, 3, 5, 6, 8, 9]

Sample Output
[1, 4, 9, 25, 36, 64, 81]
"""

from typing import List


# Time complexity O(nlogn) and Space complexity O(1)
def sorted_squared_array_brut_force(arr: List[int]) -> List[int]:
    return sorted([element * element for element in arr])


# Time complexity O(n) and Space complexity O(1)
def sorted_array_optimal(arr: List[int]) -> List[int]:
    target_arr = [0 for element in range(len(arr))]
    left_ptr = 0
    right_ptr = len(arr) - 1
    pivot_pos_of_target_array = len(target_arr) - 1

    while left_ptr <= right_ptr:
        abs_value_grabbed_by_left_ptr = abs(arr[left_ptr])
        abs_value_grabbed_by_right_ptr = abs(arr[right_ptr])

        if abs_value_grabbed_by_left_ptr > abs_value_grabbed_by_right_ptr:
            target_arr[pivot_pos_of_target_array] = (
                abs_value_grabbed_by_left_ptr * abs_value_grabbed_by_left_ptr
            )
            left_ptr += 1
            pivot_pos_of_target_array -= 1
        else:
            target_arr[pivot_pos_of_target_array] = (
                abs_value_grabbed_by_right_ptr * abs_value_grabbed_by_right_ptr
            )
            right_ptr -= 1
            pivot_pos_of_target_array -= 1

    return target_arr


if __name__ == "__main__":
    result = sorted_array_optimal([1, 2, 3, 5, 6, 8, 9])
    print(result)
    result = sorted_array_optimal([-7, -4, 1, 2, 3, 5, 6, 8, 9])
    print(result)
