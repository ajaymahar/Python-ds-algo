'''
Given an array a[ ] of size N. The task is to check if array is sorted or not.
A sorted array can either be increasingly sorted or decreasingly sorted.
Also consider duplicate elements to be sorted.

Example 1:

Input:
N = 5
a[] = {1 1 2 2 3}
Output: 1
Example 2:

Input:
N = 2
a[] = {4 2}
Output: 1


Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

'''


def isSorted(arr: list, n: int) -> int:
    # code here
    if isSortedAESC(arr, n) or isSortedDESC(arr, n):
        return 1
    return 0


def isSortedAESC(arr: list, n: int) -> bool:
    '''
    TO check provided arr/list is sorted or not.

    will start loop from index 1 till last index of an arr/list.
    will check if current index element  <  previous index element.
        if True, then arr/list is not sorted, will return False.
    if we loop through all the items and all the elements in the arr/list
    are `grater` than previous element then will return True.

    '''
    for idx in range(1, n):
        if arr[idx - 1] > arr[idx]:
            return False
    return True


def isSortedDESC(arr: list, n: int) -> bool:
    for idx in range(1, n):
        if arr[idx - 1] < arr[idx]:
            return False
    return True
