from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ms1 = defaultdict(int)
        for i in s1:
            ms1[i] += 1
        
        ms2 = defaultdict(int)
        ts = 0
        l=0
        for i in range(len(s2)):
            print(ms2)
            ms2[s2[i]] += 1
            ts += 1
            if ts > len(s1):
                while ts > len(s1):
                    ms2[s2[l]] -= 1
                    if ms2[s2[l]] == 0:
                        del ms2[s2[l]]
                    l += 1
                    ts -= 1
            if ms2 == ms1:
                return True
        return False

        