# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

# Example 1:

# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]

from typing import List  # Import List type for type hinting
from collections import Counter  # Import Counter for counting frequencies
import heapq  # Import heapq for heap operations

class Solution:  # Define a class named Solution
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  # Define a method named topKFrequent that takes a list of integers and an integer k, and returns a list of integers
        count = Counter(nums)  # Count the frequency of each element using Counter
        return heapq.nlargest(k, count.keys(), key=count.get)  # Use a heap to extract the k most frequent elements

#refactored code
from typing import List
from collections import Counter
import heapq

def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)
