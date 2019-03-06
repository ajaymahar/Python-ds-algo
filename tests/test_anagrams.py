from solutions.Arrays import anagrams
import unittest

class TestAnagrams(unittest.TestCase):
    def test_anagram_v1(self):
        test_data = {'god':'Dog', 'Public relations':'crap built on lies', 'clint east wood':'old west action'}
        for firstString, secondString in test_data.items():
            result = anagrams.anagram_v1(firstString,secondString)
            self.assertTrue(result, msg=None)


if __name__ == '__main__':
    unittest.main()