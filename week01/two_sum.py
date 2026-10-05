# LeetCode 1: Two Sum（两数之和）
# 给你一个数组 nums 和目标值 target，找出哪两个数相加等于 target，返回它们的下标。
# 例如：nums = [2, 7, 11, 15]，target = 9。因为 2 + 7 = 9，所以答案是 [0, 1]。

class Solution:
    def twoSum(self, nums: list[int], target: int):
        seen = {}
        for i, num in enumerate(nums):
            needed = target - num
            if needed in seen:
                return [seen[needed], i]
            seen[num] = i

solution = Solution()

print(solution.twoSum([2, 7, 11, 15], 26))

