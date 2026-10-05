#283 Move Zeroes
# Given an integer array nums, move all 0’s to the end of it 
# while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        index = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[index] = num
                index += 1

        for i in range(index, len(nums)): 
            nums[i] = 0

s = Solution()
nums = [0,1,0,3,12]
s.moveZeroes(nums)   

print(nums)