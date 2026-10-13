# 125. Valid Palindrome

# A phrase is a palindrome if, after converting all uppercase letters into 
# lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include 
# letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:

# Input: s = "A man"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

class Solution:
    def validPalindrome(self, s: str) -> False:
        chars = []
        for char in s:
            if char.isalnum():
                chars.append(char)
        cleaned = "".join(chars).lower()

        print(cleaned)

        left = 0
        right = len(cleaned) - 1



        while(left < right):
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1

        return True

solution = Solution()
s = "A man"
print(solution.validPalindrome(s))


