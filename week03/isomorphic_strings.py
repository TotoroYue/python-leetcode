# 205. Isomorphic Strings

# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while 
# preserving the order of characters. No two characters may map to the same character, 
# but a character may map to itself.


# Example 1:
# Input: s = "egg", t = "add"
# Output: true

# Explanation:
# The strings s and t can be made identical by:

# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.

class Solution:
    def isIsomorphic_I(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}

        if len(t) != len(s):
            return False

        for i in range(len(s)):
            a = s[i]
            b = t[i]

            if a in s_to_t and s_to_t[a] != b:
                return False

            if b in t_to_s and t_to_s[b] != a:
                return False
            
            s_to_t[a] = b
            t_to_s[b] = a
        
        return True

    def isIsomorphic_II(self, s: str, t: str) -> bool:
            s_to_t = {}
            t_to_s = {}
    
            if len(t) != len(s):
                return False
    
            for a, b in zip(s, t):
                if a in s_to_t and s_to_t[a] != b:
                    return False
    
                if b in t_to_s and t_to_s[b] != a:
                    return False
                
                s_to_t[a] = b
                t_to_s[b] = a
                
            return True

solution = Solution()
s = "egg"
t = "add"
print(solution.isIsomorphic_II(s, t))


            