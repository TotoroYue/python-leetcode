# 243 Shortest Word Distance
# Given an array of strings wordsDict and two 
# different strings that already exist in the array 
# word1 and word2, return the shortest distance between 
# these two words in the list.

# Example 1:
# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], 
# word1 = "coding", word2 = "practice"
# Output: 3

# Example 2:
# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], 
# word1 = "makes", word2 = "coding"
# Output: 1


class Solution:
    def shortestDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:
        index1 = -1
        index2 = -2
        answer = len(wordsDict)
        distance = 0

        for i in range(len(wordsDict)):
            word = wordsDict[i]
            if word == word1:
                index1 = i
            elif word == word2:
                index2 = i

            if index1 != -1 and index2 != -2:
                distance = abs(index2 - index1)
                answer = min(answer, distance)

        return answer


solution = Solution()
wordsDict = ["practice", "makes", "perfect", "coding", "maks"]
word1 = "makes"
word2 = "coding"
print(solution.shortestDistance(wordsDict, word1, word2))

