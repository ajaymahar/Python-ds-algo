#!/usr/bin/env python
'''
Env -> Python 3
    Given two strings, check to see if they are anagrams. An anagram is when the two string can be written
    using the exact same letters (so you can just rearrange the letters to get a different phrase or word)

    For example:

    "Public relations" is an anagram of "crap built on lies"
    "clint eastwood" is an anagram of "old west action" 
'''
'''
Solution 1
arguments: firstString, secondString are string type
return: bool
'''
#Checking both string are equal or not, if strings are not equal then return False
def anagram_v1(firstString: str, secondString: str) -> bool:     
    #Remove spaces and convert into lowecase
    firstString = firstString.replace(' ','').lower()
    secondString = secondString.replace(' ', '').lower()

    #Return Boolean for sorted match
    return sorted(firstString) == sorted(secondString)


#Solution 2
def anagram_v2(firstString: str, secondString: str)-> bool:
    pass
