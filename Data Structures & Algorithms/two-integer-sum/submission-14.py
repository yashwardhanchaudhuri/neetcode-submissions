class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        collection ={}
        for i in range(len(nums)):
            if target - nums[i] in collection:
                return [collection[target - nums[i]], i]
            collection[nums[i]] = i
        return []

        