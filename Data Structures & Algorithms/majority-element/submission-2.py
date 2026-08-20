from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        collection = defaultdict(int)
        maxi = 0
        for i in nums:
            collection[i] += 1
            maxi = max(maxi, collection[i])
        for i,j in collection.items():
            if j == maxi:
                return i
        return i
        