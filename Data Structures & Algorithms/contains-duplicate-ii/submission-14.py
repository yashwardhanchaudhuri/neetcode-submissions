from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        if k < 1:
            return False
        hm = defaultdict(int)
        i = 0
        # hm[nums[i]] += 1

        for j in range(0, len(nums)):
            hm[nums[j]] += 1

            if abs(i - j) > k:
                hm[nums[i]] -= 1
                i += 1

            if hm[nums[j]] == 2:
                return True
        return False     