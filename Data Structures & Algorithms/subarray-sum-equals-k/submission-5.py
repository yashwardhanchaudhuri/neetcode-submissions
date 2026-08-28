from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c = defaultdict(int)
        curr_sum = 0
        counts = 0
        c[0] = 1
        for i in nums:
            curr_sum += i
            r = curr_sum - k
            if r in c:
                counts += c[r]
            c[curr_sum] += 1
        return counts
