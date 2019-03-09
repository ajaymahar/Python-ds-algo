'''
    This is simple test we are feeding list of positive test cases and validating the expected output results.
    TC1 : pair_sum_v2([1, 3, 2, 2],4)               ==> expecte output [(1, 3), (2, 2)]
    TC2 : pair_sum_v2([1,4,45,6,10,-8],16)          ==> expecte output [(6, 10)]
    TC3 : pair_sum_v2([1, 4, 45, 6, 10, 8],16)      ==> expecte output [(6, 10)]
    TC3 : pair_sum_v2([1, 3, 2, 2],5)               ==> expecte output [(2, 3)]
    TC4 : pair_sum_v2([1,2,3,4,5,6,7,8,9],10)       ==> expecte output [(3, 7), (1, 9), (4, 6), (2, 8)]


'''
from solutions.Arrays import pair_sum as ps
positive_test = [
                ([1, 3, 2, 2], 4),
                ([1, 4, 45, 6, 10, -8], 16),
                ([1, 4, 45, 6, 10, 8], 16),
                ([1, 3, 2, 2], 5),
                ([1, 2, 3, 4, 5, 6, 7, 8, 9], 10)]

positive_test_expected_output = [
           [(1, 3), (2, 2), ],
           [(6, 10), ],
           [(6, 10), ],
           [(2, 3)],
           [(3, 7), (1, 9), (4, 6), (2, 8), ], ]


def test_pair_sum_v1():
    pass


def test_pair_sum_v2():
    result = []
    for test_data in positive_test:
        result.append(ps.pair_sum_v2(test_data[0], test_data[1]))
    assert result == positive_test_expected_output
