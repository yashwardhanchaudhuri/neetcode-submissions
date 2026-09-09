from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        mapping = defaultdict(int)
        max_char = 0
        l = 0
        ans = 0

        for i in range(len(s)):
            mapping[s[i]] += 1
            max_char = max(max_char, mapping[s[i]])

            if (i - l + 1) - max_char >= k:
                while (i - l + 1) - max_char > k:
                    mapping[s[l]] -= 1
                    l += 1
            ans = max(ans, i-l+1)
        return ans


