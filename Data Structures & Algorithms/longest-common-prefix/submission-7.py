class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = 200
        for i in range(len(strs)):
            if len(strs[i]) < min_len:
                min_len = len(strs[i])
        ans = ""
        for i in range(min_len):
            temp = strs[0][i]
            for j in strs:
                if j[i] == temp:
                    continue
                return ans
            ans += temp
        return ans
        
            


        