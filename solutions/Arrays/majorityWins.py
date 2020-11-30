'''
Given an array arr[] of size N and two elements x and y, use counter
variables to find which element appears most in the array, x or y.
If both elements have the same frequency, then return the smaller element.
Note:  We need to return the element, not its count.


Example 1:

Input:
N = 11
arr[] = {1,1,2,2,3,3,4,4,4,4,5}
x = 4, y = 5
Output: 4
Explanation:
frequency of 4 is 4.
frequency of 5 is 1.

Example 2:

Input:
N = 8
arr[] = {1,2,3,4,5,6,7,8}
x = 1, y = 7
Output: 1
Explanation:
frequency of 1 is 1.
frequency of 7 is 1.
Since 1 < 7, return 1.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

'''


def majorityWins(arr: list, x: int, y: int) -> int:
    '''
    To solve this problem we are just keeping the count of  x, y.
    created a dict called counter.

    loop through all the items in a arr/list.
        and check if curernt item is x, then increse the counter of x by 1.
        or if current item is y, then increse the counter of y by 1.
    once we done with the loop, we now  have to make a decistion which value to return.

    first will check if x,y have same frequency , if yes then will check whcih value is smaller
    and return the value.

    if counter of x is grater then will return value x,
    or return y.

    '''

    counter = {x: 0, y: 0}
    for num in arr:
        if num == x:
            counter[x] += 1
        elif num == y:
            counter[y] += 1

    if counter[x] == counter[y]:
        return x if x < y else y
    elif counter[x] > counter[y]:
        return x
    return y
