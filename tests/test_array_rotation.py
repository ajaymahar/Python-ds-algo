"""
test_data = [
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4)
            ]
expected_output = [
                    [3, 4, 5, 6, 7, 8, 9, 10, 1, 2],
                    [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
                  ]
"""

from solutions.Arrays.array_rotation import rotate_an_array_by_range_v1
from solutions.Arrays.array_rotation import rotate_an_array_by_range_v2

test_data = [
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4)
            ]
expected_output = [
                    [3, 4, 5, 6, 7, 8, 9, 10, 1, 2],
                    [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
                  ]


def test_rotate_an_array_by_range_v1():
    result = []
    for data in test_data:
        result.append(rotate_an_array_by_range_v1(data[0], data[1]))
    assert expected_output == result


def test_rotate_an_array_by_range_v2():
    result = []
    for data in test_data:
        result.append(rotate_an_array_by_range_v2(data[0], data[1]))
    assert expected_output == result
