class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        min_s = float('inf')
        total = 0

        for i in range(len(nums)):
            total += nums[i]

            if total >= target:
                while total >= target:
                    min_s = min(min_s, i-l+1)
                    total -= nums[l]
                    l += 1

        return 0 if min_s == float('inf') else min_s

