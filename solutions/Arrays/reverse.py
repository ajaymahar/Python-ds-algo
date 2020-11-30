'''
Given an array arr of size n. You need to reverse the array.

Example 1:

Input:
n = 5
arr[] = {1 1 2 2 3}
Output: 3 2 2 1 1
Example 2:

Input:
n = 2
arr[] = {4 2}
Output: 2 4

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1).
'''


def reverseArray(arr: list, n: int):
    '''
    To reverse an array we simply need to use two pointers method.

    start -> will point to starting of an array/list index.
    end -> will point to end of the array/list index.

    loop through untill `start < end`
    and swap the  elements.

    increment start index by 1 position.
    decriment end index by 1 position.
    '''
    start = 0
    end = n - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr
