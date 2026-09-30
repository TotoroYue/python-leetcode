# 26. Remove Duplicates from Sorted Array
# You are given an integer array nums sorted from smallest to largest. 
# Modify this array in place so that each distinct number appears once, keeping the same order.
# Return k, the number of distinct values. The first k positions in nums must contain those values. 
# Anything after these positions is ignored.

# Example 1:
# Input: nums = [1, 1, 2]
# Output: k = 2, nums = [1, 2, _]

# Example 2:
# Input: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# Output: k = 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]

class Solution:
    def removeDuplicates(self, nums: list[int]):
        if not nums:
            return 0;

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k += 1

        return k


solution = Solution()
nums = [1]
print(solution.removeDuplicates(nums))





