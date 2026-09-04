class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answers = set()
        for i in range(len(nums) - 2):
            s = set()
            temp = -nums[i]
            left = i + 1
            right = len(nums) - 1

            while left <= right:
                difference = temp - nums[left]
                if difference in s:
                    answers.add(tuple(sorted([difference, -temp, nums[left]])))
                s.add(nums[left])
                left += 1
        
        return [i for i in list(answers)]
        