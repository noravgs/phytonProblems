# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

# Example 1:

# Input: 
# nums = [3,4,5,6], target = 7

# Output: [0,1]
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

# Example 2:

# Input: nums = [4,5,6], target = 10

# Output: [0,2]
# Example 3:

# Input: nums = [5,5], target = 10

# Output: [0,1]

from typing import List  # Import List type for type hinting

class Solution:  # Define a class named Solution
    def twoSum(self, nums: List[int], target: int) -> List[int]:  # Define a method named twoSum that takes a list of integers and a target integer, and returns a list of integers
        num_to_index = {}  # Create a dictionary to store the indices of the elements
        
        for i, num in enumerate(nums):  # Iterate through the array with indices
            complement = target - num  # Calculate the complement of the current element
            if complement in num_to_index:  # Check if the complement exists in the dictionary
                return [num_to_index[complement], i]  # Return the indices of the complement and current element
            num_to_index[num] = i  # Store the index of the current element in the dictionary
        
        return []  # Return an empty list if no solution is found (not needed due to problem constraints)

#shorter code
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    num_to_index = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    
    return []
