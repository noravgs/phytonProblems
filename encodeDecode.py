# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

# Example 1:

# Input: ["neet","code","love","you"]

# Output:["neet","code","love","you"]
# Example 2:

# Input: ["we","say",":","yes"]

# Output: ["we","say",":","yes"]

from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        # We will use a length-prefixed encoding with a special delimiter
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        # Decode the length-prefixed encoded string
        i = 0
        decoded_strings = []
        while i < s.length:
            # Find the next delimiter
            j = s.find("#", i)
            # Extract the length of the next string
            length = int(s[i:j])
            # Extract the string itself
            decoded_strings.append(s[j + 1 : j + 1 + length])
            # Move to the next encoded string
            i = j + 1 + length
        return decoded_strings

#refactor code 
from typing import List

def encode(strs: List[str]) -> str:
    encoded_string = ""
    for s in strs:
        encoded_string += str(len(s)) + "#" + s
    return encoded_string

def decode(s: str) -> List[str]:
    i = 0
    decoded_strings = []
    while i < len(s):
        j = s.find("#", i)
        length = int(s[i:j])
        decoded_strings.append(s[j + 1 : j + 1 + length])
        i = j + 1 + length
    return decoded_strings
