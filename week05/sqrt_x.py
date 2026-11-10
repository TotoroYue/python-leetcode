# 69. Sqrt(x)
# Given a non-negative integer x, return the square root of x 
# rounded down to the nearest integer. The returned integer should be 
# non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 
# Example 1:
# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x

        while left <= right:
            root = (left + right) // 2
            if root * root <= x < (root + 1) * (root + 1):
                return root
            elif root * root > x:
                right = root - 1
            else:
                left = root + 1 


solution = Solution()
print(solution.mySqrt(9))