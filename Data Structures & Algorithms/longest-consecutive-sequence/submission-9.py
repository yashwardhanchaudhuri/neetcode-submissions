class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        count = 0

        for i in range(len(nums)):
            if nums[i] - 1 not in s:
                temp = nums[i]
                t_count = 0
                while temp in s:
                    t_count += 1
                    temp += 1
                count = max(count, t_count)
        return count 
                