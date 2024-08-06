# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# Example 2:

# Input: strs = ["x"]

# Output: [["x"]]
# Example 3:

# Input: strs = [""]

# Output: [[""]]
from typing import List  # Import List type for type hinting
from collections import defaultdict  # Import defaultdict for default dictionary with list values

class Solution:  # Define a class named Solution
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:  # Define a method named groupAnagrams that takes a list of strings and returns a list of lists of strings
        anagram_map = defaultdict(list)  # Create a dictionary to map sorted character tuples to lists of anagrams
        
        for s in strs:  # Iterate through each string in the input list
            sorted_tuple = tuple(sorted(s))  # Sort the string and convert it to a tuple
            anagram_map[sorted_tuple].append(s)  # Add the string to the list corresponding to the sorted character tuple
        
        return list(anagram_map.values())  # Return the list of anagram groups

#refactored code
from typing import List
from collections import defaultdict

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagram_map = defaultdict(list)
    
    for s in strs:
        sorted_tuple = tuple(sorted(s))
        anagram_map[sorted_tuple].append(s)
    
    return list(anagram_map.values())
