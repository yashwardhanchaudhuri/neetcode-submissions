class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # find maximum size window where each character is unique

        l = 0
        sets = set()
        best_len = 0

        for i in range(len(s)):
            if s[i] not in sets:
                sets.add(s[i])
                best_len = max(best_len, len(sets))
            else:
                while s[i] in sets:
                    sets.remove(s[l])
                    l += 1
                sets.add(s[i])
        return best_len


        
        