# 383. Ransom Note
# Given two strings ransomNote and magazine, return true 
# if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote

# Example:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true

class Solution:
    def ransom_note(self, r: str, m: str):
        count = {}
        for char in m:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        for char1 in r:
            if char1 not in count or count[char1] == 0:
                return False
            count[char1] -= 1
        return True

solution = Solution()
ransomNote = "affa"
magazine = "aab"

print(solution.ransom_note(ransomNote, magazine))

