# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count1 = {}
        count2 = {}
    
        for char in s:
            if char in count1:
                count1[char] += 1
            else:
                count1[char] = 1

        for char in t:
            if char in count2:
                count2[char] += 1
            else:
                count2[char] = 1

        if count1 == count2:
            return True
        return False

solution = Solution()
s = "aacc"
t = "caac"



print(solution.isAnagram(s,t))
    

             