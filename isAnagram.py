# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true
# Example 2:

# Input: s = "jar", t = "jam"

# Output: false

from collections import Counter  # Import Counter class for counting character occurrences

class Solution:  # Define a class named Solution
    def isAnagram(self, s: str, t: str) -> bool:  # Define a method named isAnagram that takes two strings and returns a boolean
        return Counter(s) == Counter(t)  # Compare the character counts of both strings using Counter

#refactored solution
from collections import Counter

def isAnagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)
