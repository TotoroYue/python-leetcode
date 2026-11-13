# 219. Contains Duplicate II
# Given an integer array nums and an integer k, return true 
# if there are two distinct indices i and j in the array such 
# that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true

# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true

# Example 3:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

class Solution:
    def contiansNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        lastIndex = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in lastIndex:
                if i - lastIndex[num] <= k:
                    return True
            lastIndex[num] = i
        

        return False

solution = Solution()
nums = [1,2,3,1,2,3]
k = 2
print(solution.contiansNearbyDuplicate(nums, k))