# 268. Missing Number
# Given an array nums containing n distinct numbers in the range [0, n], 
# return the only number in the range that is missing from the array.

# Example 1:
# Input: nums = [3,0,1]

# Output: 2

# Explanation:
# n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 
# 2 is the missing number in the range since it does not appear in nums.

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        full_array = list(range(n+1))
        for num in full_array:
            if num not in nums:
                print(num)

solution = Solution()
nums = [3,0,1]
solution.missingNumber(nums)

                          
