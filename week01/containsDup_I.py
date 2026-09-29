# 217. Contains Duplicate
# Given an integer array nums, return True if any value appears at least twice. 
# Return False if all values are distinct.

class Solution:
    def containsDup(self, nums: list[int]):
        if len(nums) <= 1: 
            print("AHA")
            return False
        
        seen = set()

        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False

solution = Solution()
nums = []
print(solution.containsDup(nums))


        
