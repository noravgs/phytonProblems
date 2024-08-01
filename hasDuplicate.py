# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Input: nums = [1, 2, 3, 3]

# Output: true
# Example 2:

# Input: nums = [1, 2, 3, 4]

# Output: false


from typing import List  # Import List type for type hinting

class Solution:  # Define a class named Solution
    def hasDuplicate(self, nums: List[int]) -> bool:  # Define a method named hasDuplicate that takes a list of integers and returns a boolean
        seen = set()  # Create an empty set named seen to track encountered numbers
        for num in nums:  # Iterate over each number in the list nums
            if num in seen:  # Check if the current number is already in the seen set
                return True  # If it is, return True because a duplicate is found
            seen.add(num)  # If it isn't, add the current number to the seen set
        return False  # If the loop completes without finding duplicates, return False

# def duplicate_finder (nums):
# seen = set()
# for num in nums:
# if num in seen:
# return True
# seen.add(num)
# return False