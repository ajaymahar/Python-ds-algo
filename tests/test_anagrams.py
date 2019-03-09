'''
1) rearrange the word ---> “gamanra”
testcase1 = [“anagram”, “gamanra”, True]
2) rearrange and change capitalization ---> “GraMana”
I need two tests to verify that capitalization is ignored for both input strings
testcase2a= [“anagram”, “GraMana”, True]
testcase2b= [“AnAgrAm”, “gramana”, True]
3) swap only 2 characters
a) at the start “naagram”
testcase3a= [“anagram”,“naagram”, True]
b) in the middle “anargam”
testcase3b= [“anagram”, “anargam”, True]
c) at the end “anagrma”
testcase3c= [“anagram”, “anagrma”, True]
4) test the shortest possible anagram (containing only two characters)
testcase4 = [“an”, “na”, True]

another examples:

Jim Morrison = Mr Mojo Risin
Damon Albarn = Dan Abnormal
George Bush = He bugs Gore
Clint Eastwood = Old West action
Ronald Reagan = A darn long era
Elvis = Lives
Madonna Louise Ciccone = One cool dance musician

-------------------------------------------------------------------------------------
positive_testcases = {"Ronald Reagan": "A darn long era", "Elvis": "Lives",
                      "Madonna Louise Ciccone": "One cool dance musician",
                      "Jim Morrison": "Mr Mojo Risin",
                      "Damon Albarn": "Dan Abnormal",
                      "George Bush": "He bugs Gore",
                      "Clint Eastwood": "Old West action",
                      "AnAgrAm": "gramana",
                      "an": "na"}
--------------------------------------------------------------------------------------

For simplicity, I keep my base word “anagram”
1) a completely different word
a) of same length
testcase1a = [“anagram”, “wxdcfvb”, False]
b) of different length
testcase1b = [“anagram”, “python”, False]

-------------------------------------------------------------------------------------
negative_testcases = {"anagram": "wxdcfvb", "anagramx": "python"}
--------------------------------------------------------------------------------------

'''

from solutions.Arrays import anagrams

positive_testcases = {"Ronald Reagan": "A darn long era", "Elvis": "Lives",
                      "Madonna Louise Ciccone": "One cool dance musician",
                      "Jim Morrison": "Mr Mojo Risin",
                      "Damon Albarn": "Dan Abnormal",
                      "George Bush": "He bugs Gore",
                      "Clint Eastwood": "Old West action",
                      "AnAgrAm": "gramana",
                      "an": "na"}
negative_testcases = {"anagram": "wxdcfvb", "anagramx": "python"}


def test_anagram_v1():
    for firstString, secondString in positive_testcases.items():
        assert anagrams.anagram_v1(firstString, secondString) is True

    for firstString, secondString in negative_testcases.items():
        assert anagrams.anagram_v1(firstString, secondString) is False


def test_anagram_v2():
    for firstString, secondString in positive_testcases.items():
        assert anagrams.anagram_v2(firstString, secondString) is True
    for firstString, secondString in negative_testcases.items():
        assert anagrams.anagram_v2(firstString, secondString) is False
        