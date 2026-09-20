class Solution:
    def mySqrt(self, x: int) -> int:

        left = 0
        right = x
        answer = 0
        while left <= right:
            mid = left + (right - left)//2
            sq = mid*mid

            if sq < x:
                answer = mid
                left = mid + 1
            elif sq > x:
                right = mid - 1
            else:
                return mid

        return answer
        