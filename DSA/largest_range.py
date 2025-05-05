"""
Largest Range
Write a function that takes in an array of integers and returns an array of length 2 representing the largest range of integers contained in that array.
The first number in the output array should be the first number in the range, while the second number should be the last number in the range.
A range of numbers is defined as a set of numbers that come right after each other in the set of real integers. For instance, the output array [2, 6] represents the range [2, 3, 4, 5, 6} , which is a range of length 5. Note that numbers don't need to be sorted or adjacent in the input array in order to form a range.
You can assume that there will only be one largest range.

Sample Input
array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]

Sample Output
[0, 7]
"""

# Time Complexity O(nlogn) and space complexity O(1)
def largestRange(array):
    sorted_array = sorted(array)
    start = float("inf")
    longest_seq = 0
    res = []

    if len(array) <= 1:
        return [array[0],array[0]]

    for rec in sorted_array:
        if 'curr' not in locals():
            curr = start

        if not (rec - curr == 1 or rec - curr == 0):
            seq_len = curr - start
            if seq_len > longest_seq:
                res = [start, curr]
                longest_seq = seq_len
            start = rec
        curr = rec

    seq_len = curr - start
    if seq_len > longest_seq:
        res = [start, curr]

    return res



if __name__ == "__main__":
    print(largestRange([19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, 8, 7, 6, 15, 12, 12, 2, 1, 6, 13, 14]))