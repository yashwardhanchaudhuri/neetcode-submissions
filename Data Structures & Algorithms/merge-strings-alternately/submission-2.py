class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""

        mini = min(len(word1), len(word2))

        for i in range(mini):
            s += word1[i] + word2[i]

        if len(word1) > len(word2):
            s += word1[len(word2) :]
        if len(word2) > len(word1):
            s += word2[len(word1) :]
        return s
            
        