# 169. Majority Element
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

# Example :

# Input: nums = [3,2,3]
# Output: 3

class Solution:
    def majority_ele(self, s: list[int]) -> int:
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        n = len(s)
        for char in count:
            if count[char] > n / 2:
                return char



solution = Solution()
s = [3,2,3]
print(solution.majority_ele(s))
