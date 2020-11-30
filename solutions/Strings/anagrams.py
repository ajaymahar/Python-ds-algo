#!/usr/bin/env python
'''
Env -> Python 3
    Given two strings, check to see if they are anagrams. An anagram is when
    the two string can be written using the exact same letters (so you can
    just rearrange the letters to get a different phrase or word)

    For example:
     "clint eastwood" is an anagram of "old west action"

Solution 1
arguments: firstString, secondString are string type
return: bool
'''
# Checking both string are equal or not, if strings are not equal then return
# False


def anagram_v1(firstString: str, secondString: str) -> bool:
    '''This function will take O(n log n ) time complaxity, because every
       sorting compar will take n log n time.'''
    # Remove spaces and convert into lowecase
    firstString = firstString.replace(' ', '').lower()
    secondString = secondString.replace(' ', '').lower()

    # Return Boolean for sorted match
    return sorted(firstString) == sorted(secondString)

# Solution 2


def anagram_v2(firstString: str, secondString: str) -> bool:
    '''This function will take O(n) time complaxity.
        Approach: We are using hashTable.
        hashTable = {'key':'value'} =  {'a':1, 't':2} and so on.
    '''
    # Normalize string to eliminate all the white space and converting in lower
    # case.
    firstString = firstString.replace(' ', '').lower()
    secondString = secondString.replace(' ', '').lower()

    if len(firstString) != len(secondString):
        return False
    hashTable = dict()
    # Store all the occurance of char into hash table
    for char in firstString:
        if char in hashTable:
            hashTable[char] += 1
        else:
            hashTable[char] = 1

    # Remove occurence of each char from hash table using secondString
    for char in secondString:
        if char in hashTable:
            hashTable[char] -= 1
        else:
            hashTable[char] = 1
    # Traversing the hash table to see if there is any extra char present
    for char in hashTable:
        if hashTable[char] != 0:
            return False
    return True
