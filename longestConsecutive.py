# Given an array of integers nums, return the length of the longest consecutive sequence of elements.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [2,20,4,10,3,4,5]

# Output: 4
# Explanation: The longest consecutive sequence is [2, 3, 4, 5].

# Example 2:

# Input: nums = [0,3,2,5,4,6,1,1]

# Output: 7

from typing import List

def longestConsecutive(nums: List[int]) -> int:
    num_set = set(nums)  # Convert the list to a set for O(1) lookups
    longest_streak = 0  # Variable to track the longest consecutive sequence

    for num in num_set:  # Iterate through each number in the set
        # Check if it's the start of a new consecutive sequence
        if num - 1 not in num_set:  
            current_num = num  # Start of a new sequence
            current_streak = 1  # Initialize current streak count

            # Count the length of the consecutive sequence
            while current_num + 1 in num_set:
                current_num += 1  # Move to the next number in the sequence
                current_streak += 1  # Increment the streak count
            
            # Update the longest streak if needed
            longest_streak = max(longest_streak, current_streak)

    return longest_streak  # Return the length of the longest consecutive sequence
