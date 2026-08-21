import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        high = random.choice(nums)
        left = [x for x in nums if x < high]
        right = [x for x in nums if x > high]
        mid = [x for x in nums if x == high]
        return self.sortArray(left) + mid + self.sortArray(right)



        