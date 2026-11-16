# 697. Degree of an Array
# Given a non-empty array of non-negative integers nums, 
# the degree of this array is defined as the maximum frequency of any one of its elements.

# Your task is to find the smallest possible length of a (contiguous) 
# subarray of nums, that has the same degree as nums.

# Example 1:
# Input: nums = [1,2,2,3,1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.

# Example 2:
# Input: nums = [1,2,2,3,1,4,2]
# Output: 6
# Explanation: 
# The degree is 3 because the element 2 is repeated 3 times.
# So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.

class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        count = {}
        first = {}
        last = {}

        for i in range(len(nums)):
            num = nums[i]

            if num not in count:
                count[num] = 0
                first[num] = i

            count[num] += 1
            last[num] = i

        degree = max(count.values())

        shortest = len(nums)

        for num in count:
            if count[num] == degree:
                length = last[num] - first[num] + 1
                shortest = min(shortest, length)

        return shortest

solution = Solution()
nums = [1,2,2,2,3,1]
print(solution.findShortestSubArray(nums))


