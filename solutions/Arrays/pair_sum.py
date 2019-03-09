'''
Array Pair Sum
Given an integer array, output all the unique pairs that sum up to a specific value k.
So the input:
pair_sum([1,3,2,2],4)
would return 2 pairs:
(1,3)
(2,2)
'''


# Solution 1
def pair_sum_v1(array: list, k: int) -> list:
    pass


''' Solution 2
    Using hashing
    
    loop through each element in array
    find target by subtracting with element with k
    example:
    array = [1,3,2,2]
    k = 4
    element = array[index]
    target = k - element
    target = 4 - 1
    target would be 3

    if :
         "target" is not in "seen" hash set, then will add "element" into "seen" hash set
    else: (if target is in "seen" hash set, well we just found one pair :) )
        will add pair (min(element, target), max(element, target)) # example (1,3)

    at last when we went through all the elements of an array will just print the "output"
'''


def pair_sum_v2(array: list, k: int) -> list:
    if len(array) < 2:
        return
    # create hash set called seen and output
    seen = set()
    output = set()
    for element in array:
        target = k - element
        if target not in seen:
            seen.add(element)
        else:
            output.add((min(element, target), max(element, target)))
    return list(output)
