'''
Move all zeroes to end of array
Given an array of random numbers, Push all the
zero’s of a given array to the end of the array.
For example, if the given arrays is
{1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0}, it should be changed to
{1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0}.
The order of all other elements should be same.

Time Complexity: O(n) where n is number of elements in input array.

Auxiliary Space: O(1)

Method explained:

    # Traverse the array. If element
    # Encountered is non-zero, then
    # Replace the element at index
    # Increment 'count' by 1
    # Now all non-zero elements have been
    # shifted to front and 'count' is set
    # as index of first 0. Make all
    # elements 0 from count to end.
'''


def push_zero_to_end(array: list) -> list:
    count = 0
    for index in range(len(array)):
        if array[index] != 0:
            array[count] = array[index]
            count += 1
    while (count < len(array)):
        array[count] = 0
        count += 1
    return array
