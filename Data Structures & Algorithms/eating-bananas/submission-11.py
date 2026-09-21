class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eat_all(arr, rate):
            hrs = 0
            for i in range(len(arr)):
                hrs += (arr[i] + rate - 1)//rate
            return hrs
        
        right = max(piles)
        left = 1
        
        while left <= right:
            mid = left + (right - left)//2
            time = eat_all(piles, mid)
            if time > h:
                left = mid + 1
            else:
                right = mid - 1

        return left