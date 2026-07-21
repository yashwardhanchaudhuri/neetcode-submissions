class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        collection = set()
        for i in nums:
            if i not in collection:
                collection.add(i)
            else:
                return True
        return False
        