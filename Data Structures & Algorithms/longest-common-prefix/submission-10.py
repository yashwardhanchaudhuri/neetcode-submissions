class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min(len(s) for s in strs)
        ans = ""
        for i in range(min_len):
            temp = strs[0][i]
            for j in strs:
                if j[i] == temp:
                    continue
                return ans
            ans += temp
        return ans
        
            


        