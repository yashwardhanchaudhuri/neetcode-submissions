from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicti = Counter(nums)
        outs = dict(sorted(dicti.items(), key = lambda x : x[1], reverse = True))
        # print(dict(outs))
        return list(outs.keys())[:k]