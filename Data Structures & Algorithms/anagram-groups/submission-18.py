from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collection = defaultdict(list)
        for i in strs:
            collection[str(sorted(i))].append(i)
        return list(collection.values())
        