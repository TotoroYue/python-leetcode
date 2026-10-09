# 383. Ransom Note
# Given two strings ransomNote and magazine, return true 
# if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.
# Example :

# Input: ransomNote = "aa", magazine = "aab"
# Output: true

class Solution:
    def ransom_note(self, ransomNote: str, magazine: str) -> bool:
        count = {}
        for char in magazine:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        for char in ransomNote:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1

        return True


solution = Solution()
ransomNote = "aa"
magazine = "aab"

print(solution.ransom_note(ransomNote, magazine))