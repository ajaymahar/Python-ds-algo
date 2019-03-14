"""
Given a array and range, you need to rotate it by range.
For Example 1:
    Input :  arr[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            range = 4
    Output : arr[] = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4] 

Example 2:
    Input :  arr[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            range = 2
    Output : arr[] = [3, 4, 5, 6, 7, 8, 9, 10, 1, 2] 
"""


def rotate_an_array_by_range_v1(array: list, r: int) -> list:
    """ Using python built in list function to solve the problem
        Time Complaxity:
            O(n)
        Storage:
            O(r)

    """
    first_list = array[:r]      # Store first part of the array   
    second_list = array[r:]     # Store second part of the array
    second_list.extend(first_list)  # Combined both an array
    return second_list


def rotate_an_array_by_range_v2(array: list, r: int) -> list:
    """Reverse array in parts to solve the problem
    Time Compx: O(n)
    Example: array[1, 2, 3, 4, 5], r=2
    Reverse first part of an "array" till "r"
        array = [2, 1, 3, 4, 5]
    Reverse second part of an "array" till end
        array = [2, 1, 5, 4, 3]
    Now reverse all the array from 0 to end
        array = [3, 4, 5, 1, 2]
    """
    end = len(array) - 1        # Find the end index of an array
    reverse(array, 0, r - 1)    # reverse till the r
    reverse(array, r, end)      # reverse from r to end
    reverse(array, 0, end)      # reverse hole array
    return array                # return the result


def reverse(array: list, start: int, end: int):
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
