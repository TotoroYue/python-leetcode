# 14. Longest Common Prefix
# Write a function to find the longest common 
# prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

class Solution:
    def longestComPrefix(self, s: list[str]) -> str:
        prefix = s[0]
        for word in s[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
        return prefix

    def longestComPrefix_i(self, strs: list[str]) -> str:
        if not strs:
            return ""

        for i in range(len(strs[0])):
            for word in strs[1:]:
                if i >= len(word) or strs[0][i] != word[i]:
                    return strs[0][:i]
        


solution = Solution()
strs = ["flower","flow","floight","flo"]
print(solution.longestComPrefix_i(strs))

    