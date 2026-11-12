# 34. Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in non-decreasing order, 
# find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = 0
        right = len(nums) - 1
        res = [-1,-1]

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                res[0] = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                res[1] = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return res

    def searchRange_II(self, nums, target):

        def find_bound(find_first):
            left = 0
            right = len(nums) - 1
            res = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    res = mid

                    if find_first:
                        right = mid - 1
                    else:
                        left = mid + 1

                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return res

        return [find_bound(True), find_bound(False)]

solution = Solution()
nums = [5,7,7,8,8,10]
target = 6
print(solution.searchRange(nums, target))


