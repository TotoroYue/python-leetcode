# 344 Reverse String
# Write a function that reverses a string. 
# The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]


class Solution:
    def reverseStr(self, s: str):
        left = 0
        right = len(s) - 1
        temp = s[left]

        while(left < right):
            temp = s[left]
            s[left] = s[right]
            s[right] = temp

            left += 1
            right -= 1


solution = Solution()
s = ["h","e","l","l","o"]
print(solution.reverseStr(s))

