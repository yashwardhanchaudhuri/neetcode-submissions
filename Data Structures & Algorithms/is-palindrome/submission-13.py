class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ""
        for i in s.lower():
            if i.isalnum():
                x+=i
        return x == x[::-1]
        