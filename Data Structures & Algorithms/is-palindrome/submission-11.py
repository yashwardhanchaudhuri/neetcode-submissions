class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(s.lower().split())
        x = ""
        for i in s:
            if i.isalnum():
                x+=i
        return x == x[::-1]
        