class Solution:
    def isValid(self, s: str) -> bool:
        #
        t = []
        pairs = ['{}', '[]', '()']
        if len(s) <= 1: return False
        for i in range(len(s)):
            if len(t) == 0:
                t.append(s[i])
            else:
                if t[-1] + s[i] in pairs:
                    t.pop()
                else:
                    t.append(s[i])
        
        return True if len(t) == 0 else False