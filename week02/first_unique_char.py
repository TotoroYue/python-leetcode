# 387. First Unique Character in a String

# Given a string s, find the first non-repeating character in it and return its index. 
# If it does not exist, return -1.
 
# Example 1:
# Input: s = "leetcode"
# Output: 0

# Explanation:
# The character 'l' at index 0 is the first character that does not occur at any other index.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for char in s:
            if char in count:
                count[char] += 1       
            else:
                count[char] = 1

        for i, target in enumerate(s):
            if count[target] == 1:
                return i;
        return -1   

solution = Solution()
s = "lleetcode"
print(solution.firstUniqChar(s))