# 350 Intersection of Two Arrays II

# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must appear as many times as it shows in both arrays 
# and you may return the result in any order.

# Example:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

class Solution:
    def interOfTwoArryII(self, nums1: list[int], nums2: list[int]) -> list[int]:
        counts = {}
        result = []

        for char in nums1:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1

        for char in nums2:
            if char in counts and counts[char] > 0:
                counts[char] -= 1
                result.append(char)

        return result;

solution = Solution()
nums1 = [4,9,5,9]
nums2 = [9,4,9,8,4]
print(solution.interOfTwoArryII(nums1, nums2))



                
