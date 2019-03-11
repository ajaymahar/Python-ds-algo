
from solutions.Arrays import move_all_zeroes as mod

test_data = [1, 2, 4, 0, 6, 8, 0, 0, 8, 6, 0, 8, 0, 0, 8, 6, ]
expected_output = [1, 2, 4, 6, 8, 8, 6, 8, 8, 6, 0, 0, 0, 0, 0, 0]


def test_push_zero_to_end():
    assert mod.push_zero_to_end(test_data) == expected_output
