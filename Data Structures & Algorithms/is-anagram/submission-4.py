from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        si = [0]*26
        ti = [0]*26

        for i in range(len(s)):
            si[ord(s[i]) - ord('a')] += 1
        for j in range(len(t)):
            ti[ord(t[j]) - ord('a')] += 1


        return si == ti

        