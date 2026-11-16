# 409. Longest Palindrome
# Given a string s which consists of lowercase or 
# uppercase letters, return the length of the longest 
# palindrome that can be built with those letters.

# Letters are case sensitive, for example, 
# "Aa" is not considered a palindrome.

# Example 1:
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be 
# built is "dccaccd", whose length is 7.

# Example 2:
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be 
# built is "a", whose length is 1.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        for char in s:
            if char not in count:
                count[char] = 0
            count[char] += 1

        length = 0
        has_odd = False

        for times in count.values():
            if times % 2 ==0:
                length += times
            else:
                length += times - 1
                has_odd = True

        if has_odd == True:
            length += 1

        return length

solution = Solution()
s = "aaabccccdd"
print(solution.longestPalindrome(s))