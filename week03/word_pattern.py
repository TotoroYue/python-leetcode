# 290. Word Pattern
# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a 
# letter in pattern and a non-empty word in s. Specifically:

# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.


class Solution:
    def wordPatttern(self, patttern: str, s: str) -> bool:
        words = s.split()

        if len(patttern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for char, word in zip(patttern, words):
            if char in char_to_word and char_to_word[char] != word:
                return False

            if word in word_to_char and word_to_char[word] != char:
                return False

            char_to_word[char] = word
            word_to_char[word] = char

        return True

solution = Solution()
pattern = "abba"
s = "dog cat cat do"
print(solution.wordPatttern(pattern, s))



